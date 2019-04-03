import time
from pathlib import Path
from sweetest.globals import g
from sweetest.config import _testcase, _elements, _report
from sweetest.lib.excel import Excel


def mkdir(p):
    '''
    创建目录
    :param p: 目录名
    '''

    p = Path(p)
    # 若不存在该目录，则创建它
    if not p.is_dir():
        p.mkdir()


def path():
    '''
    初始化测试过程中的各类文件，包括元素表、测试用例、excel形式的report、html形式的report
    '''

    # 检查是否存在以下目录，不存在则新建
    for p in ('report', 'htmlreport', 'snapshot'):
        mkdir(p)

    g.start_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

    # 元素表文件
    g.elements_file = Path('element') / (g.project_name + '-' + _elements + '.xlsx')

    # 测试用例文件
    g.testcase_file = Path('testcase') / (g.project_name + '-' + _testcase + '.xlsx')

    # 待测试的测试用例表单
    g.testcase_workbook = Excel(g.testcase_file)
    g.sheet_names = g.testcase_workbook.get_sheet(g.sheet_name)

    # excel格式的报告
    g.report_file = Path('report') / (g.project_name + '-' + _report + '@' + g.start_time + '.xlsx')

    # 把excel用例的内容复制到excel报告中
    Excel.copy_excel(g.testcase_file, g.report_file)
    g.report_workbook = Excel(g.report_file)

    # html格式的报告
    g.htmlreport_file = Path('htmlreport') / (g.project_name + '-' + _report + '@' + g.start_time + '.html')

    # html格式的报告模板
    g.html_template = Path('template/template.html')
