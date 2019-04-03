import sys
import json
from pathlib import Path
from sweetest.globals import g
from sweetest.lib.elements import have_elem
from sweetest.lib.excel import Excel
from sweetest.lib.csv import read_csv, write_csv
from sweetest.lib.utility import data2dict
from sweetest.lib.log import logger
from sweetest.config import all_keywords, comma_lower


def analyze_record(record, data, d, i):
    '''
    将csv文件中的数据转换成dict结构
    :param record: dict结构变量
    :param data: csv文件中的数据
    :param d: 第几行
    :param i: 第几列
    :return:
    '''
    k = data[0][i]
    # 若record中未有值
    if record.get(k, None):
        if isinstance(record[k], str):
            record[k] = [record[k]]
        record[k].append(d[i])
    # 若record中已有值
    else:
        record[k] = d[i]
    return record


def read_record(data_file):
    '''
    读取csv文件中的记录，转换为dict
    :param data_file: csv文件
    :return: csv文件中的全局变量，结构为dict
    外部csv测试数据文件：
    最后字段!=flag，变量值全部读取使用
    最后字段=flag，读取flag!=Y的变量值 使用，读取后置flag=Y，下次自动化测试时不再使用该值
    '''

    encoding = None
    try:
        data = read_csv(data_file, encoding='utf-8')
        encoding = 'utf-8'
    except:
        data = read_csv(data_file)

    record = {}
    if data[0][-1].lower() != 'flag':
        for d in data[1:]:
            for i in range(len(data[0])):
                record = analyze_record(record, data, d, i)
    else:
        for d in data[1:]:
            if d[-1] != 'Y':
                for i in range(len(data[0][:-1])):
                    record = analyze_record(record, data, d, i)
                d[-1] = 'Y'
                write_csv(data_file, data, encoding=encoding)
                break
    return record


def check_keyword(kw):
    '''
    将测试用例中的 ’操作‘值 解析为对应的关键字
    :param kw: 测试用例中的’操作‘值
    :return: 对应的关键字
    '''

    try:
        keyword = all_keywords.get(kw)
        return keyword
    except:
        logger.exception('操作关键字:%s 不存在' % kw)
        exit()


def elementInCase(page, element):
    '''
    确定测试用例中的page、custom、element
    :param page: 测试用例中的页面值
    :param element: 测试用例中的元素值
    :return: page、frame、element
    '''

    # 若测试用例中，page为空，则取当前页面
    if not page:
        page = g.current_page
    # 若测试用例中，element为空，则frame为空，直接返回
    if not element:
        return page, '', element
    # 若是用例片段、变量赋值，则frame为空，直接返回
    if page in ('SNIPPET', '用例片段') or element in ('变量赋值',):
        return page, '', element

    # 对元素进行拆分，以|做多个元素的分隔符
    elements = element.split('|')
    # 用例中的element只有1个
    if len(elements) == 1:
        # 从元素表中查找对应的custom(frame)
        custom, el = have_elem(page, element)
        g.current_page = page
        return page, custom, el
    # 用例中的element有多个
    else:
        els = []
        for _element in elements:
            # 从元素表中查找对应的custom(frame)
            custom, el = have_elem(page, _element.strip())
            els.append(el)
        g.current_page = page
        return page, custom, els


def elements_format(data):
    '''
    将 dict 组成的 list，处理转换为 二元dict
    :param data: excel中读取的元素，结构为 dict 的 list
    :return: 元素，结构为 二元dict
    元素表的结构：二元dict
    {
        page1^element1:{
                    'page' : '通用',         #元素所在页面
                    'element' : 'name#',    #元素名称
                    'by' : 'xpath',         #元素定位方式
                    'value' : '#',          #元素定位值
                    'custom' : '',          #用于页面有 frame 的情况，如果元素不在默认 frame，需填写该元素的 frame id
                    'remark' : ''},         #备注说明
        page1^element2:{
                    'page' : '通用',
                    'element' : 'password#',
                    'by' : 'xpath',
                    'value' : '#',
                    'custom' : '' ,
                    'remark' : ''},
        ...
    }
    '''
    elements = {}
    page = ''
    custom = ''
    for d in data:
        # page为空时，自动继承上一个元素的值
        # page为新值时，custom清空
        if d['page'].strip():
            page = d['page']
            custom = ''
        else:
            d['page'] = page

        # 在同一个 page 层级下，若下层元素的 custom为空， 自动继承上一个元素的值
        if d.get('custom', '').strip():
            custom = d['custom']
        else:
            d['custom'] = custom
        # ^只是个分隔符，也可以用-
        elements[d['page'] + '^' + d['element']] = d
    return elements


def testsuite_format(data):
    '''
    将元素为 dict 的 list，处理转换为 testcase 的 list
    :param data: 转换前的测试用例集
    :return: 转换后的测试用例集
    转换后testcase 的格式：
        {
        'id': 'Login_001',                    #用例编号
        'title': 'Login OK',                  #用例标题
        'condition': '',                      #前置条件
        'designer': 'Leo',                    #设计者
        'flag': '',                           #自动化标记
        'result': '',                         #用例结果
        'remark': '',                         #备注
        'steps':
            [
                {
                'control': '',                   #测试步骤逻辑控制
                'no': 1,                         #测试步骤
                'keyword': '输入',                #关键字
                'page': '产品管系统登录页',         #页面
                'custom': ,                      #frame
                'element': '元素1,元素2',          #元素
                'data': '变量1=值1,变量2=值2',     #测试数据
                'expected': '变量1=值1,变量2=值2', #预期结果
                'output': '变量1=值1,变量2=值2',   #输出数据
                'score': '',                     #测试结果
                'remark': ''                     #备注
                },
                {……}
                ……
            ]
        }

    testsuite 的格式：[testcase1,testcase2,testcase3,...]
    '''

    testsuite = []
    testcase = {}

    for d in data:
        # 如果用例编号不为空，则为新的用例
        if str(d['id']).strip():
            # 如果 testcase 非空，则添加到 testsuite 里，并重新初始化 testcase
            if testcase:
                testsuite.append(testcase)
                testcase = {}
            for key in ('id', 'title', 'condition', 'designer', 'flag', 'result', 'remark'):
                testcase[key] = d[key]
            # 测试用例优先级默认为M（中）
            testcase['priority'] = d['priority'] if d['priority'] else 'M'
            # 测试步骤是 dict组成的list
            testcase['steps'] = []
        # 如果测试步骤不为空，则为有效步骤，否则用例解析结束
        no = str(d['step']).strip()
        if no:
            step = {}
            step['control'] = ''
            '''
            ^ 表示 if 语句
            > 表示 then 语句
            < 表示 else 语句
            # ?
            '''
            if no[0] in ('^', '>', '<', '#'):
                step['control'] = no[0]
                step['no'] = no
            else:
                step['no'] = str(int(d['step']))
            for key in ('keyword', 'page', 'element', 'data', 'expected', 'output', 'score', 'remark'):
                step[key] = d.get(key, '')
            # 确定测试用例中的page、custom、element
            step['page'], step['custom'], step['element'] = elementInCase(
                step['page'], step['element'])

            testcase['steps'].append(step)

    if testcase:
        testsuite.append(testcase)
    return testsuite


def data_format(data):
    '''
    将用英文逗号 或 双英文逗号 隔开的数据处理为 dict
    :param data: 测试用例中的测试数据、预期结果、输出结果，用 英文逗号 或 双英文逗号 隔开（若数据中带有英文逗号，需转义 \,）
    :return: 处理后的数据，结构是dict
    '''

    # 将转义字符 \, ， 替换为： # $%^&
    data = data.replace('\\,', comma_lower)
    data_list = []
    data_dict = {}
    # 若数据中带双英文逗号，以此做分隔符
    if ',,' in data:
        data_list = data.split(',,')
    # 否则以英文逗号做分隔符
    else:
        if data:
            data_list = data.split(',')
    for data in data_list:
        # 分割第一个'='号，将变量及值存在list中
        d = data.split('=', 1)
        # 将之前替换的  # $%^&， 替换为： ,
        d[-1] =d[-1].replace(comma_lower, ',')
        if len(d) == 1:
            # 如果没有=号分割，说明只有内容，默认赋值给 text
            data_dict['text'] = d[0]
        elif len(d) == 2:
            d[0] = d[0].strip()  # 清除 <元素属性> 2边的空格
            data_dict[d[0]] = d[1]
        else:
            raise Exception(
                '错误: 测试用例中的数据存在错误！')
    return data_dict


def parse_elements():
    '''
    从excel文件中获取、解析元素表，存储到g.elements中
    '''

    try:
        g.elements = elements_format(data2dict(Excel(g.elements_file).read('elements')))
    except:
        logger.exception('*** 解析元素表失败 ***')
        g.code = -1
        sys.exit(g.code)


def parse_suite(sheet_name):
    '''
    从excel文件中获取测试用例集，进行转换、解析、分解
    :param sheet_name: excel表单中的测试用例集
    :return: base、end、setup、teardown、normal 5类用例，将snippet存储在g.snippet中
    '''

    # 从excel文件中获取、转换测试用例集
    testsuite = import_suite(sheet_name)
    # 将测试用例解析为可执行参数
    testsuite = analyze_suite(testsuite)
    # 将测试用例集分解为base、end、setup、teardown、normal、snippet 6类用例
    base_testcase, end_testcase, setup_testcase, teardown_testcase, normal_testcase = decompose_suite(testsuite)

    return testsuite, base_testcase, end_testcase, setup_testcase, teardown_testcase, normal_testcase


def parse_var(sheet_name):
    '''
    从外部csv文件中读取全局变量
    :param sheet_name: csv文件名称的一部分
    :return: 全局变量的值
    '''
    try:
        # 如果测试数据文件存在，则从该文件里读取一行数据，赋值到全局变量列表里
        data_file = Path('data') / (g.project_name + '-' + sheet_name + '.csv')
        if data_file.is_file():
            g.var = read_record(data_file)
    except:
        logger.exception('*** 初始化全局变量失败 ***')
        g.code = -1
        sys.exit(g.code)


def import_suite(sheet_name):
    '''
    从excel文件中获取、转换测试用例集
    :param sheet_name: excel表单形式的测试用例集
    :return: 返回转换后的测试用例集
    testsuite 是 testcase的list
    testcase是dict，其中steps是由测试步骤组成的list（步骤是dict结构）
    '''
    try:
        testsuite = testsuite_format(data2dict(g.testcase_workbook.read(sheet_name)))
        logger.info('从Excel中读取测试用例集:\n' +
                    json.dumps(testsuite, ensure_ascii=False, indent=4))
        logger.info('从Excel中读取测试用例集成功！')
        return testsuite
    except:
        logger.exception('*** 从Excel中读取测试用例集失败 ***')
        g.code = -1
        sys.exit(g.code)


def analyze_suite(testsuite):
    '''
    将测试用例解析为可执行参数，如:打开首页，解析为：OPEN 127.0.0.1
    :param testsuite: 解析前的测试用例集
    :return: 解析后的测试用例集
    解析后的testcase：
    {
        'id': 'Login_001',                    #用例编号
        'title': 'Login OK',                  #用例标题
        'condition': '',                      #前置条件
        'designer': 'Leo',                    #设计者
        'flag': '',                           #自动化标记
        'result': '',                         #用例结果
        'remark': '',                         #备注
        'steps':
            [
                {
                'control': '',                  #测试步骤逻辑控制
                'no': 1,                        #测试步骤
                'keyword': '输入',               #关键字
                'page': '产品管系统登录页',        #页面
                'custom': ,                     #frame
                'element': [元素1,元素2],         #元素
                'data': {变量1：值1,变量2:值2},    #测试数据
                'expected':{变量1：值1,变量2:值2}, #预期结果
                'output': {变量1：值1,变量2:值2},  #输出数据
                'score': '',                     #测试结果
                'remark': ''                     #备注
                },
                {……}
                ……
            ]
    }
    '''

    try:
        for testcase in testsuite:
            for step in testcase['steps']:
                # 测试用例中的’操作‘值解析为对应的关键字
                step['keyword'] = check_keyword(step['keyword'])
                # 将用英文逗号 或 双英文逗号 隔开的数据处理为 dict
                step['data'] = data_format(str(step['data']))
                step['expected'] = data_format(str(step['expected']))
                step['output'] = data_format(str(step['output']))
        logger.debug('测试用例集已完成解析:\n' + str(testsuite))
        return testsuite
    except:
        logger.exception('*** 解析测试用例集失败 ***')
        g.code = -1
        sys.exit(g.code)


def decompose_suite(testsuite):
    '''
    将测试用例集分解为base、end、setup、teardown、normal、snippet 6类用例，并且将用例片段存储在g.snippet中
    :param testsuite: 测试用例集
    :return: base_testcase, end_testcase, setup_testcase, teardown_testcase, normal_testcases
    g.snippet格式：
    {
      id1: testcase1,
      id2: testcase2,
      ...
    }
    '''

    # base 在整个测试套件前执行一次
    base_testcase = {}
    # end 在整个测试套件后执行一次
    end_testcase = {}
    # setup 在每个测试用例执行之前执行一次
    setup_testcase = {}
    # teardown 在每个测试用例执行之后执行一次
    teardown_testcase = {}
    # 普通测试用例
    normal_testcases = []
    for testcase in testsuite:
        if testcase['condition'].lower() == 'base':
            base_testcase = testcase
            testcase['flag'] = 'N'
        elif testcase['condition'].lower() == 'end':
            end_testcase = testcase
            testcase['flag'] = 'N'
        elif testcase['condition'].lower() == 'setup':
            setup_testcase = testcase
            testcase['flag'] = 'N'
        elif testcase['condition'].lower() == 'teardown':
            teardown_testcase = testcase
            testcase['flag'] = 'N'
        elif testcase['condition'].lower() == 'snippet':
            g.snippet[testcase['id']] = testcase
            testcase['flag'] = 'N'
        # 自动化标志flag ！= n，表示是自动化测试用例
        elif testcase['flag'].lower() not in ['n', ]:
            # 用例总数统计
            g.results['testAll'] += 1
            # 根据筛选条件，把不需要执行的测试用例跳过
            for k, v in g.conditions.items():
                if not isinstance(v, list):
                    v = [v]
                if testcase[k] not in v:
                    testcase['flag'] = 'N'
                    testcase['result'] = 'Skip'
                    for step in testcase.get('steps'):
                        step['score'] = '-'
                    # 跳过用例数统计
                    g.results['testSkip'] += 1
                    break
            if testcase['flag'] != 'N':
                normal_testcases.append(testcase)
        # 非自动化测试用例
        else:
            testcase['result'] = 'Skip'
            for step in testcase.get('steps'):
                step['score'] = '-'
            # 用例总数统计
            g.results['testAll'] += 1
            # 跳过用例数统计
            g.results['testSkip'] += 1

    return base_testcase, end_testcase, setup_testcase, teardown_testcase, normal_testcases
