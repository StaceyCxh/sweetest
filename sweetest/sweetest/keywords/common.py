from copy import deepcopy
from sweetest.globals import g
from sweetest.lib.elements import get_elem
from sweetest.lib.log import logger
from sweetest.lib.parse import data_format
from sweetest.lib.utility import replace, replace_list
import sweetest.lib.gentest
import re
import json


def execute(step):
    # 先处理循环结束条件
    condition = ''
    for k in ('循环结束条件', 'condition'):
        if step['data'].get(k):
            condition = step['data'].get(k)
            del step['data'][k]
    if condition.lower() in ('成功', 'pass'):
        condition = 'Pass'
    elif condition.lower() in ('失败', 'fail'):
        condition = 'Fail'

    element = step['element']
    times = 1
    _element = element.split('*')

    # snippet 执行失败是否退出标志
    flag = True
    if element[-1] == '*':
       flag = False

    if len(_element) >= 2:
        element = _element[0]
        times = int(_element[1])

    key = g.snippet[element].get('id')

    for k, v in step['data'].items():
        g.var[k] = replace(v)

    # 初始化测试片段执行结果
    result = 'Pass'
    if element != '变量赋值':
        for t in range(times):
            name = key+'_1'
            g.snippet[name] = deepcopy(g.snippet[key])
            sweetest.lib.gentest.genSnippest(name)
            try:
                getattr(sweetest.lib.gentest.TestClass, name)()
            except:
                result = 'Fail'

            step['snippets'].append(g.snippet[name]['steps'])
            delattr(sweetest.lib.gentest.TestClass, name)

            # 用例片段执行失败时
            if result != 'Pass':
                # 循环退出条件为失败，则直接返回，返回结果是 Pass
                if condition == 'Fail':
                    return 'Pass'
                # 如果没有结束条件，且失败直接退出标志位真，则返回结果
                if not condition and flag:
                    return result
            # 用例片段执行成功时
            else:
                # 如果循环退出条件是成功，则直接返回，返回结果是 Pass
                if condition == 'Pass':
                    return 'Pass'
        # 执行结束，还没有触发循环退出条件，则返回结果为 Fail
        if condition:
            return 'Fail'
    return result, step['snippets']


def sql(step):
    element = step['element']
    el, _sql = get_elem(element)

    logger.info('SQL: %s' % repr(_sql))
    # 获取连接参数
    el, value = get_elem(step['page'] + '-' + 'config')
    arg = data_format(value)

    if step['page'] not in g.db.keys():
        g.db[step['page']] = DB(arg)
    if _sql.lower().startswith('select'):
        row = g.db[step['page']].fetchone(_sql)
        logger.info('SQL result: %s' % repr(row))
        if not row:
            raise Exception('*** Fetch None ***')
    else:
        g.db[step['page']].execute(_sql)

    result = {}
    if _sql.lower().startswith('select'):
        keys = _sql[6:].split('FROM')[0].split('from')[0].strip().split(',')
        for i,k in enumerate(keys):
            keys[i] = k.split(' ')[-1]
        result = dict(zip(keys, row))
        logger.info('keys result: %s' % repr(result))

    data = step['data']
    if not data:
        data = step['expected']
    if data:
        for key in data:
            logger.info('key: %s, expect: %s, real: %s' %
                        (repr(key), repr(data[key]), repr(result[key])))
            if data[key].startswith('*'):
                assert data[key][1:] in result[key]
            else:
                assert data[key] == result[key]

    output = step['output']
    if output:
        logger.info('output: %s' % repr(output))
        for key in output:
            g.var[key] = result[output[key]]


def call(step):
    output = step['output']
    if output:
        logger.info('Call function: %s' % repr(output))
        for key in output:
            value = output[key].split('.')
            s = 'from sweetest.lib' + ' import ' + value[0].strip()
            exec(s)
            p = re.compile(r'[(](.*?)[)]', re.S)
            params = re.findall(p, value[1])[0]
            if len(params):
                params = params.split(',')
                replace_list(params)
                if len(params) == 1:
                    params = params[0]
                g.var[key] = getattr(eval(value[0].strip()), value[1].split('(')[0].strip())(params)
            else:
                g.var[key] = getattr(eval(value[0].strip()), value[1].split('(')[0].strip())()
            logger.info('g.var[' + key +']=' + str(g.var[key]))
