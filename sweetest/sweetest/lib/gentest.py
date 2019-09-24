import unittest
from time import sleep
from pathlib import Path
from sweetest.globals import g
from sweetest.lib.windows import w
from sweetest.lib.log import logger
from sweetest.keywords import web, common, mobile, http
from sweetest.config import web_keywords, mobile_keywords, http_keywords
from sweetest.lib.utility import replace_dict, replace_list, replace


class _Factory(object):
    def __init__(self, name, case):
        self._name = name
        self.testcase = case

    def __call__(self, *args, **kwargs):
        if_result = ''
        if self.testcase:
            self.testcase['result'] = 'Pass'
            for index, step in enumerate(self.testcase.get('steps')):
                # if 为否，不执行 then 语句
                if step['control'] == '>' and not if_result:
                    step['score'] = '-'
                    continue

                # if 为真，不执行 else 语句
                if step['control'] == '<' and if_result:
                    step['score'] = '-'
                    continue

                logger.info('执行测试步骤: %s|%s|%s' %
                            (step['no'], step['keyword'], step['element']))

                try:
                    # 变量替换
                    replace_dict(step['data'])
                    replace_dict(step['expected'])

                    if isinstance(step['element'], str):
                        step['element'] = replace(step['element'])
                    elif isinstance(step['element'], list):
                        step['element'] = replace_list(step['element'])

                    # 处理强制等待时间
                    t = step['data'].get('等待时间')
                    if t:
                        del step['data']['等待时间']
                        sleep(float(t))

                    if g.platform.lower() in ('desktop',) and step['keyword'] in web_keywords:
                        if step['keyword'] not in ('MESSAGE', '对话框'):
                            # 判断页面是否已和窗口做了关联，如果没有，就关联当前窗口，如果已关联，则判断是否需要切换
                            w.switch_window(step['page'])
                            # 切换 frame 处理，支持变量替换
                            frame = replace(step['custom'])
                            w.switch_frame(frame)
                            sleep(2)

                        # 根据关键字调用关键字实现
                        getattr(web, step['keyword'].lower())(step)

                    elif g.platform.lower() in ('ios', 'android') and step['keyword'] in mobile_keywords:
                        # 切換 context 處理
                        context = replace(step['custom']).strip()
                        current_context = w.switch_context(context)

                        if w.current_context.startswith('WEBVIEW'):
                            # 切换标签页
                            tab = step['data'].get('标签页')
                            if tab:
                                del step['data']['标签页']
                                g.driver.switch_to_window(w.windows[tab])
                            logger.info('Current Context: %s' %
                                        repr(w.current_context))

                        # 根据关键字调用关键字实现
                        getattr(mobile, step['keyword'].lower())(step)

                    elif step['keyword'] in http_keywords:
                        # 根据关键字调用关键字实现
                        getattr(http, step['keyword'].lower())(step)

                    elif step['keyword'].lower() == 'execute':
                        if step['page'] in ('SNIPPET', '用例片段'):
                            step['snippets'] = []
                            result, step['snippets'] = getattr(
                                common, step['keyword'].lower())(step)

                            logger.info('用例片段执行结果:\n')
                            logger.info(result)

                            self.testcase['result'] = result

                            if result != 'Pass':
                                break
                        # elif step['page'] in ('SCRIPT', '脚本'):
                        #     # 判断页面是否已和窗口做了关联，如果没有，就关联当前窗口，如果已关联，则判断是否需要切换
                        #     w.switch_window(step['page'])
                        #     # 切换 frame 处理，支持变量替换
                        #     frame = replace(step['custom'])
                        #     w.switch_frame(frame)
                        #     common.script(step)

                    else:
                        # 根据关键字调用关键字实现
                        getattr(common, step['keyword'].lower())(step)

                    logger.info('执行测试步骤通过: %s|%s|%s' %
                                (step['no'], step['keyword'], step['element']))
                    step['score'] = 'OK'

                    # if 语句结果赋值
                    if step['control'] == '^':
                        if_result = True

                    # 操作后，等待0.2秒
                    sleep(0.2)
                except Exception as exception:
                    file_name = g.project_name + '-' + g.sheet_name + '-' + g.start_time + \
                        '#' + self.testcase['id'] + \
                        '-' + str(step['no']) + '.png'
                    snapshot_file = str(Path('snapshot') / file_name)

                    if g.platform.lower() in ('desktop',) and step['keyword'] in web_keywords:
                        try:
                            g.driver.get_screenshot_as_file(snapshot_file)
                        except:
                            logger.exception('*** 保存截图失败！ ***')

                    elif g.platform.lower() in ('ios', 'android') and step['keyword'] in mobile_keywords:
                        try:
                            g.driver.switch_to_default_content()
                            w.current_context = 'NATIVE_APP'
                            g.driver.get_screenshot_as_file(snapshot_file)
                        except:
                            logger.exception('*** 保存截图失败！ ***')

                    logger.exception('执行测试步骤失败: %s|%s|%s' %
                                    (step['no'], step['keyword'], step['element']))
                    step['score'] = 'NO'

                    # if 语句结果赋值
                    if step['control'] == '^':
                        if_result = False
                        continue

                    self.testcase['result'] = 'Fail'
                    step['remark'] += str(exception)
                    break

            if self.testcase['condition'] in ['', None]:
                self.testcase['setup'] = g.setup_testcase

            if self.testcase['condition'] in ['teardown', 'TEARDOWN']:
                case = {}
                case['id'] = self.testcase.get('id')
                case['title'] = self.testcase.get('title')
                case['result'] = self.testcase.get('result')
                case['steps'] = self.testcase.get('steps')
                g.teardowns.append(case)

            assert self.testcase['result'] == 'Pass'

def create(name, testcase):
    '''
    方法工厂
    :param name: 方法名称
    :param testcase: 方法
     python 使用名字空间记录变量，名字空间实际上是一个dict；
    局部名字空间：locals，只读、不可修改；locals()返回局部名字空间的拷贝；
    全局名字空间：globals，可修改；globals()返回实际的全局名字空间，非拷贝；
    '''

    # 设置全局变量
    globals()[name] = _Factory(name, testcase)


class TestClass(unittest.TestCase):
    '''
    继承于unittest的测试类
    '''

    # 用@classmethod标签标记类初始化方法。每个类只会执行一次该方法。
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        if g.exist == 1:
            try:
                if g.platform.lower() in ('desktop',):
                    w.close()
            except:
                logger.exception('清除测试环境失败！')

    def setUp(self):
        pass

    def tearDown(self):
        pass


def gentest():
    '''
    为测试类动态生成测试用例
    '''

    if g.base_testcase:
        name = 'setUpClass'
        create(name, g.base_testcase)
        setattr(TestClass, name, eval(name))

    if g.end_testcase:
        name = 'tearDownClass'
        create(name, g.end_testcase)
        setattr(TestClass, name, eval(name))

    if g.setup_testcase:
        name = 'setUp'
        create(name, g.setup_testcase)
        setattr(TestClass, name, eval(name))

    if g.teardown_testcase:
        name = 'tearDown'
        create(name, g.teardown_testcase)
        setattr(TestClass, name, eval(name))

    for case in g.normal_testcases:
        name = 'test_' + case.get('id')
        create(name, case)
        setattr(TestClass, name, eval(name))

    for key in g.snippet:
        name = key
        create(name, g.snippet[key])
        setattr(TestClass, name, eval(name))


def genSnippest(name):
    '''
    生成用例片段对应的方法
    :param name: 用例片段的标题
    '''
    create(name, g.snippet[name])
    setattr(TestClass, name, eval(name))
