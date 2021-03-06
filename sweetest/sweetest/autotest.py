import sys, time, unittest, json
from sweetest.globals import g
from sweetest.lib.windows import w
from sweetest.lib.log import logger
from sweetest.lib.path import path
from sweetest.lib.parse import parse_elements, parse_suite, parse_var
import sweetest.lib.gentest
from sweetest.lib.gentest import gentest
from sweetest.lib.myrunner import myTextTestRunner
from sweetest.lib.report import htmlreport
from sweetest.lib.db import DB
from sweetest.lib.mail import Mail, Pop3
from sweetest.lib.dingtalk import DingTalk


class AutoTest(object):
    '''
    自动化测试类，包含4个类方法，用于规划自动化测试过程
    '''

    def __init__(self):
        super(AutoTest, self).__init__()

    @classmethod
    def plan(cls):
        '''
        自动化测试过程规划：初始化路径 -> 解析元素 -> 逐个执行测试套件 -> 生成报告  -> 发送邮件/钉钉群通知
        '''

        # 初始化目录和各文件
        path()
        # 初始化数据库
        # g.db = DB()
        '''
        从 Excel 获取、解析元素表
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
        parse_elements()

        # 记录测试开始时间，格式 yyyy-mm-dd HH:MM:SS
        g.results['beginTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # g.db.insert_result(g.results['beginTime'])
        # 逐个执行测试套件
        for sheet_name in g.sheet_names:
            # g.db.insert_suite(sheet_name)
            g.current_sheet_name = sheet_name
            # 测试准备工作：解析测试用例集 -> 解析全局变量 -> 初始化浏览器和窗口 -> 初始化 unittest.testcase
            cls.ready()
            # 执行测试
            cls.test()

            # 测试结果写入excel报告中
            g.report_workbook.write()
            # 存储测试结果
            cls.output()
        # 测试结果赋值
        g.results['testResult'] = g.suite
        # 生成html格式的报告
        htmlreport()

        # 发送钉钉群消息
        # DingTalk().send_markdown()
        # 发送邮件
        # Mail().sendmail()

    @staticmethod
    def ready():
        '''
        测试准备工作：解析测试用例集 -> 解析全局变量 -> 初始化浏览器和窗口 -> 初始化 unittest.testcase
        :param sheet_name: excel格式的测试用例集
        testcase 的格式：
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
                'no': 1,                        #测试步骤
                'keyword': '输入',               #关键字
                'page': '产品管系统登录页',        #页面
                'custom': ,                     #frame
                'element': [元素1,元素2],         #元素
                'data': {变量1：值1,变量2:值2},    #测试数据
                'expected':{变量1：值1,变量2:值2}, #预期结果
                'output': {变量1：值1,变量2:值2},  #输出数据
                'score': '',                     #测试结果
                'remark': '',                    #备注
                'snippets': [[{},{},...],[],...] #调用的用例片段各步骤
                },
                {……}
                ……
            ]
        }

        testsuite 的格式：[testcase1,testcase2,testcase3,...]
        '''

        # 1.从 Excel 获取、解析测试用例集
        parse_suite(g.current_sheet_name)
        # 2.从 Csv 获取、解析全局变量
        parse_var(g.current_sheet_name)

        # 3.初始化浏览器和窗口
        try:
            g.set_driver()
            w.init()
        except:
            logger.exception('*** 初始化浏览器或窗口失败 ***')
            g.code = -1
            sys.exit(g.code)

        # 4.初始化 unittest.testcase
        gentest()

    @staticmethod
    def test():
        '''
        初始化suite和runner，运行测试
        '''
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(sweetest.lib.gentest.TestClass))
        runner = myTextTestRunner(verbosity=2)
        runner.run(suite)

    @staticmethod
    def output():
        '''
        将测试后的用例详情存储到g.suite
        :param suiteName: 用例集名称
        g.suite格式：
        [{
            "testsuite": "baidu",           #测试用例集
            "testcases": [                  #测试用例
            {
                    "id": "BAIDU_001",                   #用例ID
                    "title": "搜索：自动化测试",            #用例标题
                    "result": "成功",                     #用例结果
                    "setup": {                           #用例准备工作（即setup用例内容）
                        "id": "HOME_001",
                        "title": "打开百度",
                        "result": "Pass",
                        "steps": [
                            {
                                "control": "",
                                "no": "1",
                                "keyword": "EXECUTE",
                                "page": "用例片段",
                                "element": "SNIPPET_003",
                                "data": {},
                                "expected": {},
                                "output": {},
                                "score": "OK",
                                "remark": "",
                                "custom": "",
                                "snippets": [
                                ]
                            }
                        ]
                    },
                    "steps": [
                        {
                            "control": "",                      #测试步骤逻辑控制符（if、else、then）
                            "no": "1",                          #测试步骤
                            "keyword": "INPUT",                 #关键字
                            "page": "百度搜索页面",               #测试页面
                            "element": "百度搜索页面^搜索框",      #测试元素
                            "data": {                           #测试数据
                                "text": "自动化测试",
                                "text1": ""
                            },
                            "expected": {},                     #预期结果
                            "output": {},                       #输出数据
                            "score": "OK",                      #执行结果
                            "remark": "",                       #备注说明
                            "custom": ""                        #frame信息
                        },
                        {...},
                        ...
                    ],
                    "teardown": {                           #用例清理工作（即teardown用例内容）
                        "id": "HOME_002",
                        "title": "打开百度",
                        "result": "Pass",
                        "steps": [
                            {
                                "control": "",
                                "no": "1",
                                "keyword": "EXECUTE",
                                "page": "用例片段",
                                "element": "SNIPPET_003",
                                "data": {},
                                "expected": {},
                                "output": {},
                                "score": "OK",
                                "remark": "",
                                "custom": "",
                                "snippets": [
                                ]
                            }
                        ]
                    },
            },
            {...},
            ...
        }
        {   "testsuite": "baidu",           #测试用例集
            "testcases": [  ]                #测试用例
        }]
        '''

        suite = {}
        suite['testsuite'] = g.current_sheet_name
        suite['testcases'] = []
        for i, case in enumerate(g.normal_testcases):
            testcase = {}
            testcase['id'] = case['id']
            testcase['title'] = case['title']
            setup = {}
            if 'setup' in case.keys():
                setup['id'] = case['setup'].get('id')
                setup['title'] = case['setup'].get('title')
                setup['result'] = case['setup'].get('result')
                setup['steps'] = case['setup'].get('steps')
            testcase['setup'] = setup
            testcase['steps'] = case['steps']
            if g.teardowns:
                testcase['teardown'] = g.teardowns[i]
            if case['result'] == 'Pass':
                # 通过用例数统计
                g.results['testPass'] += 1
                testcase['result'] = '成功'
            else:
                g.results['testFail'] += 1
                # 失败用例数统计
                testcase['result'] = '失败'
            suite['testcases'].append(testcase)
        for case in g.testsuite:
            if case['result'] == 'Skip':
                testcase = {}
                testcase['id'] = case['id']
                testcase['title'] = case['title']
                testcase['result'] = '跳过'
                testcase['steps'] = case['steps']
                suite['testcases'].append(testcase)
        g.suite.append(suite)
        # g.db.update_result(g.results)

    @staticmethod
    def get_result():
        logger.info('测试结果:\n' +
                    json.dumps(g.results, ensure_ascii=False, indent=4))
        return g.results


