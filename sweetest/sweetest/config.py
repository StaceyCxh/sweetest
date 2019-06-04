# web关键字
web_keywords = {
    '打开': 'OPEN',
    'OPEN': 'OPEN',
    '检查': 'CHECK',
    'CHECK': 'CHECK',
    '#检查': 'NOTCHECK',
    '#CHECK': 'NOTCHECK',
    '输入': 'INPUT',
    'INPUT': 'INPUT',
    '点击': 'CLICK',
    'CLICK': 'CLICK',
    '选择': 'SELECT',
    'SELECT': 'SELECT',
    '移动到': 'MOVE',
    'MOVE': 'MOVE',
    '右击': 'CONTEXT_CLICK',
    'CONTEXT_CLICK': 'CONTEXT_CLICK',
    '双击': 'DOUBLE_CLICK',
    'DOUBLE_CLICK': 'DOUBLE_CLICK',
    '拖拽': 'DRAG_AND_DROP',
    'DRAG_AND_DROP': 'DRAG_AND_DROP',
    '滑动': 'SWIPE',
    'SWIPE': 'SWIPE',
    '脚本': 'SCRIPT',
    'SCRIPT': 'SCRIPT',
    '对话框': 'MESSAGE',
    'MESSAGE': 'MESSAGE',
    '上传文件': 'UPLOAD',
    'UPLOAD': 'UPLOAD',
    '刷新': 'REFRESH',
    'REFRESH': 'REFRESH',
    '获取': 'OBTAIN',
    'OBTAIN': 'OBTAIN',
    '判断': 'JUDGE',
    'JUDGE': 'JUDGE'
}
# 通用关键字
common_keywords = {
    '执行': 'EXECUTE',
    'EXECUTE': 'EXECUTE',
    'SQL': 'SQL',
    '调用': 'CALL',
    'CALL': 'CALL'
}
# http关键字
http_keywords = {
    'GET': 'GET',
    'POST': 'POST',
    'PUT': 'PUT',
    'PATCH': 'PATCH',
    'DELETE': 'DELETE',
    'OPTIONS': 'OPTIONS'
}
# 移动关键字
mobile_keywords = {
    '检查': 'CHECK',
    'CHECK': 'CHECK',
    '#检查': 'NOTCHECK',
    '#CHECK': 'NOTCHECK',
    '输入': 'INPUT',
    'INPUT': 'INPUT',
    '填写': 'SET_VALUE',
    'SET_VALUE': 'SET_VALUE',
    '点击': 'CLICK',
    'CLICK': 'CLICK',
    '轻点': 'TAP',
    'TAP': 'TAP',
    '按键码': 'PRESS_KEYCODE',  # Android 特有，常见代码 HOME:3, 菜单键：82，返回键：4
    'PRESS_KEYCODE': 'PRESS_KEYCODE',
    '滑动': 'SWIPE',
    'SWIPE': 'SWIPE',
    '划线': 'LINE',
    'LINE': 'LINE',
    '划线解锁': 'LINE_UNLOCK',
    'LINE_UNLOCK': 'LINE_UNLOCK',
    '摇杆': 'ROCKER',
    'ROCKER': 'ROCKER',
    '滚动': 'SCROLL',  # iOS 专用
    'SCROLL': 'SCROLL',
    '拖拽': 'DRAG_AND_DROP',
    'DRAG_AND_DROP': 'DRAG_AND_DROP',
    '摇晃': 'SHAKE',  # 貌似 Android 上不可用
    'SHAKE': 'SHAKE',
    '快速滑动': 'FLICK',
    'FLICK': 'FLICK',
    '滑动元素': 'FLICK_ELEMENT',
    'FLICK_ELEMENT': 'FLICK_ELEMENT',
    '长按': 'LONG_PRESS',
    'LONG_PRESS': 'LONG_PRESS',
    '缩小': 'PINCH',
    'PINCH': 'PINCH',
    '放大': 'ZOOM',
    'ZOOM': 'ZOOM',
    '隐藏键盘': 'HIDE_KEYBOARD',  # iOS 专用
    'HIDE_KEYBOARD': 'HIDE_KEYBOARD',
    '命名标签页': 'TAB_NAME',
    'TAB_NAME': 'TAB_NAME'
}
# 关键字
all_keywords = {}
for keywords in (web_keywords, common_keywords, http_keywords, mobile_keywords):
    all_keywords = dict(all_keywords, **keywords)

# 文件名后缀
_testcase = 'TestCase'  # '测试用例'
_elements = 'Elements'  # '页面元素表'
_report = 'Report'  # '测试结果'

# 特殊符号的转换别名
# 英文逗号
comma_lower = '#$%^&'
# 中文逗号
comma_upper = '&^%$#'
# 加号
addition = '&$&^&@#'
# 减号
subtraction = '&$&^&@~'
# 乘号
multiplication = '&$&^&@@'
# 除号
division = '&$&^&@^'
# 取余
residual = '&$&^&@$'
# (号
lparenthesis = '&$&^&@!'
# )号
rparenthesis = '&$&^&@?'
# < 号
lbrackets = '!@&^&$&'
# > 号
rbrackets = '?@&^&$&'

# 解析元素或用例时，中英文映射
header = {
    '用例编号': 'id',
    '用例标题': 'title',
    '前置条件': 'condition',
    '测试步骤': 'step',
    '操作': 'keyword',
    '页面': 'page',
    '元素': 'element',
    '测试数据': 'data',
    '预期结果': 'expected',
    '输出数据': 'output',
    '优先级': 'priority',
    '设计者': 'designer',
    '自动化标记': 'flag',
    '步骤结果': 'score',
    '用例结果': 'result',
    '备注': 'remark',
    '定位方式': 'by',
    '定位值': 'value',
    '自定义': 'custom'
}

element_wait_timeout = 5  # 等待元素出现超时时间，单位：秒
page_flash_timeout = 90  # 页面刷新超时时间，单位：秒

# 数据库名称
db_name = "AutoTestDB"
# 数据库表初始脚本
db_initsql = 'db.sql'

# 钉钉相关设置
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=fec1cc32dfeaf0c2c012b042f979402379ec101e3d4cc7a2d8f0855758cd92e1'
title = '自动化测试报告'

# 邮件相关设置
'''
mail_server = "smtp.gmail.com"
mail_port = 587
mail_username = "staceycxh@gmail.com"
mail_password = "dhikvjfkvvjksryh"
'''
'''
mail_server = "smtp.qq.com"
mail_port = 465
mail_username = "446909219@qq.com"
mail_password = "dhikvjfkvvjksryh"
'''

mail_server = "smtp.exmail.qq.com"
mail_port = 465
mail_username = "chenxiaohua@youmi.net"
mail_password = "yD5zsKWACZixSJJo"

mail_receiver = "chenxiaohua@youmi.net"
mail_subject = "自动化测试报告"
