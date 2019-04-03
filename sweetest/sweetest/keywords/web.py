from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from sweetest.globals import g
from sweetest.lib.elements import get_elem
from sweetest.lib.windows import w
from sweetest.lib.locator import locating_element
from sweetest.lib.log import logger
from sweetest.lib.utility import str2int, str2float


class Common():
    @classmethod
    def title(cls, data, output):
        expected = data['text']
        real = g.driver.title

        detail_check(expected, real)
        # 只能获取到元素标题
        for key in output:
            g.var[key] = g.driver.title

    @classmethod
    def current_url(cls, data, output):
        expected = data['text']
        real = g.driver.current_url

        detail_check(expected, real)
        # 只能获取到元素 url
        for key in output:
            g.var[key] = g.driver.current_url


def open(step):
    element = step['element']
    el, value = get_elem(element)
    if step['data'].get('清理缓存', '') or step['data'].get('cookie', ''):
        g.driver.delete_all_cookies()
    if step['data'].get('打开方式', '') == '新标签页' or step['data'].get('mode', '').lower() == 'tab':
        js = "window.open('%s')" % value
        g.driver.execute_script(js)
        # 判断是否打开了新的窗口，并将新窗口添加到所有窗口列表里
        all_handles = g.driver.window_handles
        for handle in all_handles:
            if handle not in w.windows.values():
                w.register(step, handle)
    else:
        if step['data'].get('打开方式', '') == '新浏览器' or step['data'].get('mode', '').lower() == 'browser':
            w.close()
            g.set_driver()
            w.init()
        g.driver.get(value)
        w.open(step)
    sleep(0.5)


def detail_check(expected, real):
    logger.info('DATA:%s' % repr(expected))
    logger.info('REAL:%s' % repr(real))
    if isinstance(expected, str):
        if expected.startswith('^'):
            if expected.endswith('$'):
                assert real == expected[1:-1]
            elif expected.endswith('*'):
                assert real.startswith(expected[1:-1])
            else:
                assert real.startswith(expected[1:])
        elif expected.startswith('*'):
            if expected.endswith('$'):
                assert real.endswith(expected[1:-1])
            else:
                assert expected[1:] in real
        elif expected.endswith('$'):
            assert real.endswith(expected[:-1])
        elif expected.endswith('*'):
            assert expected[:-1] in real
        else:
            assert expected == real
    elif isinstance(expected, int):
        real = str2int(real)
        assert real == round(expected)
    elif isinstance(expected, float):
        t, p1 = str2float(real)
        d, p2 = str2float(expected)
        p = min(p1, p2)
        assert round(t, p) == round(d, p)
    elif expected is None:
        assert real == ''


def check(step):
    data = step['data']
    if not data:
        data = step['expected']

    element = step['element']
    element_location = locating_element(element)
    if '#' in element:
        e_name = element.split('#')[0] + '#'
    else:
        e_name = element
    by = g.elements[e_name]['by']
    output = step['output']

    if by in ('title', 'current_url'):
        getattr(Common, by)(data, output)

    else:
        for key in data:
            # 预期结果
            expected = data[key]

            if key == 'text':
                real = element_location.text
            else:
                real = element_location.get_attribute(key)

            detail_check(expected, real)

        # 获取元素其他属性
        get_Ouput(step, element_location)


def notcheck(step):
    data = step['data']
    if not data:
        data = step['expected']

    element = step['element']
    element_location = locating_element(element)

    if g.elements[element]['by'] == 'title':
        assert data['text'] != g.driver.title


def get_Ouput(step, element_location):
    output = step['output']
    for key in output:
        if output[key] == 'text':
            g.var[key] = element_location.text
        elif output[key] in ('text…', 'text...'):
            if element_location.text.endswith('...'):
                g.var[key] = element_location.text[:-3]
            else:
                g.var[key] = element_location.text
        else:
            g.var[key] = element_location.get_attribute(output[key])


def input(step):
    data = step['data']
    element = step['element']
    element_location = locating_element(element)

    if step['data'].get('清除文本', '') == '否' or step['data'].get('clear', '').lower() == 'no':
        pass
    else:
        element_location.clear()

    for key in data:
        if key.startswith('text'):
            if isinstance(data[key], tuple):
                element_location.send_keys(*data[key])
            elif element_location:
                element_location.send_keys(data[key])
            sleep(0.5)


def click(step):
    element = step['element']
    if isinstance(element, str):
        element_location = locating_element(element, 'CLICK')
        if element_location:
            element_location.click()
    elif isinstance(element, list):
        for _e in element:
            element_location = locating_element(_e, 'CLICK')
            element_location.click()
            sleep(0.5)
    sleep(0.5)

    # 获取元素其他属性
    get_Ouput(step, element_location)

    # 判断是否打开了新的窗口，并将新窗口添加到所有窗口列表里
    all_handles = g.driver.window_handles
    for handle in all_handles:
        if handle not in w.windows.values():
            w.register(step, handle)


def select(step):
    pass


def move(step):
    actions = ActionChains(g.driver)
    element = step['element']
    el = locating_element(element)
    actions.move_to_element(el)
    actions.perform()
    sleep(0.5)


def context_click(step):
    actions = ActionChains(g.driver)
    element = step['element']
    el = locating_element(element)
    actions.context_click(el)
    actions.perform()
    sleep(0.5)


def double_click(step):
    actions = ActionChains(g.driver)
    element = step['element']
    el = locating_element(element)
    actions.double_click(el)
    actions.perform()
    sleep(0.5)


def drag_and_drop(step):
    actions = ActionChains(g.driver)
    element = step['element']
    source = locating_element(element[0])
    target = locating_element(element[1])
    actions.drag_and_drop(source, target)
    actions.perform()
    sleep(0.5)


def swipe(step):
    actions = ActionChains(g.driver)
    element = step['element']
    data = step['data']

    source = locating_element(element)
    x = data.get('x', 0)
    y = data.get('y', 0)
    actions.drag_and_drop_by_offset(source, x, y)
    actions.perform()
    sleep(0.5)


def script(step):
    element = step['element']
    el, value =get_elem(element)
    g.driver.execute_script(value)


def message(step):
    data = step['data']
    text = data.get('text', '')
    element = step['element']
    el, value = get_elem(element)

    if value.lower() in ('确认', 'accept'):
        g.driver.switch_to_alert().accept()
    elif value.lower() in ('取消', '关闭', 'cancel', 'close'):
        g.driver.switch_to_alert().dismiss()
    elif value.lower() in ('输入', 'input'):
        g.driver.switch_to_alert().send_keys(text)
        g.driver.switch_to_alert().accept()
    logger.info('--- Switch Frame: Alert')
    w.frame = 'Alert'


def upload(step):
    import win32com.client

    data = step['data']
    element = step['element']
    element_location = locating_element(element)
    file_path = data.get('text', '') or data.get('file', '')

    element_location.click()
    sleep(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(file_path)
    sleep(2)
    shell.Sendkeys("{ENTER}")
    sleep(2)


def refresh(step):
    g.driver.refresh()
