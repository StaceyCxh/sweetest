from selenium import webdriver
from sweetest.config import element_wait_timeout, page_flash_timeout


class Global(object):
    def __init__(self):
        super(Global, self).__init__()
        self.project_name = ''
        self.sheet_name = ''
        self.desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome'}
        self.server_url = ''
        self.code = 0
        self.var = {}
        self.snippet = {}
        self.current_page = '通用'
        self.db = {}
        self.http = {}
        self.baseurl = {}
        self.driver = ''
        self.action = {}
        self.results = {
            "testAll": 0,
            "testPass": 0,
            "testFail": 0,
            "testSkip": 0,
            "beginTime": "",
            "totalTime": "",
            "testResult": []
        }
        self.suite = []
        self.teardowns = []

    def set_driver(self):
        if self.platform.lower() == 'desktop':
            if self.browserName.lower() == 'ie':
                self.driver = webdriver.Ie()
            elif self.browserName.lower() == 'firefox':
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
            elif self.browserName.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                prefs = {}
                prefs["credentials_enable_service"] = False
                prefs["profile.password_manager_enabled"] = False
                options.add_experimental_option("prefs", prefs)
                options.add_argument('disable-infobars')
                options.add_argument('--ignore-certificate-errors')
                options.add_experimental_option(
                    "excludeSwitches", ["ignore-certificate-errors"])
                self.driver = webdriver.Chrome(chrome_options=options)
            else:
                raise Exception(
                    '错误: 浏览器不被支持或浏览器名称错误：%s' % self.browserName)
            # 等待元素超时时间
            self.driver.implicitly_wait(element_wait_timeout)  # seconds
            # 页面刷新超时时间
            self.driver.set_page_load_timeout(page_flash_timeout)  # seconds

        elif self.platform.lower() in ['ios', 'android']:
            from appium import webdriver as appdriver
            self.driver = appdriver.Remote(self.server_url, self.desired_caps)

    def close(self):
        self.driver.close()


g = Global()

# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
g.project_name = 'UT'
# g.project_name = 'Baidu'
# g.project_name = 'InterUT'

# 单 sheet 页面模式
# g.sheet_name = 'baidu'
g.sheet_name = 'Advertising'
# g.sheet_name = 'Access'


# sheet 页面匹配模式，支持首部或结尾带*，表示模糊匹配
# g.sheet_name = 'TestCase*'

# sheet 页面列表模式
# g.sheet_name = ['TestCase', 'test']

# 环境配置信息
# Chrome
g.desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome'}
g.platform = g.desired_caps.get('platformName', '')
g.browserName = g.desired_caps.get('browserName', '')
g.server_url = ''

# 按条件执行,支持筛选的属性有：'id', 'title', 'designer', 'priority'
g.conditions = {}
