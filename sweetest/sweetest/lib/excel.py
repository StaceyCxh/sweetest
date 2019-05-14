import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font, colors
from openpyxl.styles.fills import PatternFill
from sweetest.globals import g
import re


DarkRedFill = PatternFill("solid", fgColor="CD3700")
RedFill = PatternFill("solid", fgColor="EE0000")
GreenFill = PatternFill("solid", fgColor="006400")
OrangeFill = PatternFill("solid", fgColor="EE4000")
BlueFill = PatternFill("solid", fgColor="0000FF")
GrayFill = PatternFill("solid", fgColor="7A7A7A")

Fills = {
    'Fail': RedFill,
    'Pass': GreenFill,
    'Skip': BlueFill,
    'Block': OrangeFill,
}


class Excel(object):
    '''
    Excel类，用于处理excel
    '''
    def __init__(self, file_name):
        '''
        初始化excel文件，可读写
        :param file_name: excel文件名
        '''
        super(Excel, self).__init__()
        self.length = 0
        self.workbook = load_workbook(file_name)

    def get_sheet(self, sheet_name):
        '''
        匹配获取excel的标签页名
        :param sheet_name: 标签页名，可模糊匹配
        :return: 匹配的标签页名
        '''
        names = []
        flag = 0b00
        if isinstance(sheet_name, str):
            if sheet_name.startswith('^'):
                flag = flag | 0b01
                sheet_name = sheet_name[1:]
            elif sheet_name.startswith('*'):
                flag = flag | 0b100
                sheet_name = sheet_name[1:]

            if sheet_name.endswith('$'):
                flag = flag | 0b10
                sheet_name = sheet_name[:-1]
            elif sheet_name.endswith('*'):
                flag = flag | 0b100
                sheet_name = sheet_name[:-1]

            if flag == 0b00 or (flag & 0b11 == 0b11):
                for name in self.workbook.get_sheet_names():
                    if sheet_name == name:
                        names.append(name)
                        break
            elif flag & 0b01:
                for name in self.workbook.get_sheet_names():
                    if name.startswith(sheet_name):
                        names.append(name)
            elif flag & 0b10:
                for name in self.workbook.get_sheet_names():
                    if name.endswith(sheet_name):
                        names.append(name)
            else:
                for name in self.workbook.get_sheet_names():
                    if sheet_name in name:
                        names.append(name)

        elif isinstance(sheet_name, list):
            names = sheet_name
        else:
            raise Exception('错误: 无效的excel表单名: %s' % sheet_name)

        return names

    def read(self, sheet_name):
        '''
        获取excle表单中的数据
        :param sheet_name: Excel 中标签页名称
        :return: 表单中的数据，格式为二维list，[[],[]……]
        '''

        sheet = self.workbook.get_sheet_by_name(sheet_name)
        data = []
        for row in sheet.rows:
            d = []
            for cell in row:
                if cell.value is None:
                    value = ''
                else:
                    value = cell.value
                d.append(value)
            data.append(d)
        return data

    def write(self):
        '''
        将测试结果写入excel报告中，并进行格式化
        '''
        sheet = self.workbook.get_sheet_by_name(g.current_sheet_name)
        # 首行用例标题设置红色底色、字体白色
        for cell in sheet[1]:
            cell.fill = DarkRedFill
            cell.font = Font(color=colors.WHITE)
        m = 0
        n = 2
        while m < len(g.testsuite):
            self.length = 0

            cell_result = '%s%d' % (chr(111), n)
            sheet[cell_result].value = g.testsuite[m].get('result', '')
            # 用例结果列设置底色
            if sheet[cell_result].value:
                sheet[cell_result].fill = Fills[sheet[cell_result].value]
                sheet[cell_result].font = Font(color=colors.WHITE)

            for step in g.testsuite[m].get('steps'):
                cell_keyword = '%s%d' % (chr(101), (n+self.length))
                cell_score = '%s%d' % (chr(110), (n+self.length))
                cell_remark = '%s%d' % (chr(112), (n+self.length))
                sheet[cell_score].value = step.get('score', '')
                sheet[cell_score].font = Font(color=colors.BLACK)
                if sheet[cell_score].value == 'NO':
                    sheet[cell_score].fill = GrayFill
                    sheet[cell_score].font = Font(color=colors.WHITE)
                sheet[cell_remark].value = step.get('remark', '')
                sheet[cell_remark].font = Font(color=colors.BLACK)

                z = 1
                if sheet[cell_keyword].value in ['EXECUTE', 'execute', '执行']:
                    is_match = 1
                    while is_match:
                        cell_condition = '%s%d' % (chr(99), (n + self.length + z))
                        if re.findall(r'SNIPPET_(.+?)', str(sheet[cell_condition].value)):
                            z += 1
                        else:
                            is_match = 0
                self.length = self.length + z

            m = m + 1
            n = n + self.length

        self.workbook.save(g.report_file)

    def insert_rows(self, rows, row, no):
        sheet = self.workbook.get_sheet_by_name(g.current_sheet_name)
        nrows = len(rows.get('steps'))
        n = 2
        is_match = 0
        while n < (sheet.max_row + 1):
            i = '%s%d' % (chr(97), n)
            if row == sheet[i].value:
                while n < (sheet.max_row + 1):
                    j = '%s%d' % (chr(99), n)
                    k = '%s%d' % (chr(100), n)
                    if sheet[j].value in [None] and str(sheet[k].value)[-1] == no:
                        n += 1
                        is_match = 1
                        break
                    n += 1
                if is_match == 1:
                    break
                n += 1
            n += 1
        sheet.insert_rows(n, nrows)
        for index, step in enumerate(rows.get('steps')):
            cell_no = '%s%d' % (chr(100), (n + index))
            cell_keyword = '%s%d' % (chr(101), (n + index))
            cell_page = '%s%d' % (chr(102), (n + index))
            cell_element = '%s%d' % (chr(103), (n + index))
            cell_data = '%s%d' % (chr(104), (n + index))
            cell_expected = '%s%d' % (chr(105), (n + index))
            cell_output = '%s%d' % (chr(106), (n + index))
            cell_score = '%s%d' % (chr(110), (n + index))
            cell_remark = '%s%d' % (chr(112), (n + index))
            sheet[cell_no].value = step.get('no', '')
            sheet[cell_keyword].value = step.get('keyword', '')
            sheet[cell_page].value = step.get('page', '')
            sheet[cell_element].value = str(step.get('element', ''))
            sheet[cell_data].value = str(step.get('data', ''))
            sheet[cell_expected].value = str(step.get('expected')) if step.get('expected', '') else None
            sheet[cell_output].value = str(step.get('output')) if step.get('output', '') else None
            sheet[cell_score].value = step.get('score', '')
            sheet[cell_score].font = Font(color=colors.BLACK)
            if sheet[cell_score].value == 'NO':
                sheet[cell_score].fill = GrayFill
                sheet[cell_score].font = Font(color=colors.WHITE)
            sheet[cell_remark].value = step.get('remark', '')
            cell_title = '%s%d' % (chr(99), (n + index))
            sheet[cell_title].value = rows.get('id')

        self.workbook.save(g.report_file)

    @classmethod
    def copy_excel(cls, filename1, filename2):
        '''
        复制excel文件
        :param filename1: 被复制的文件
        :param filename2: 复制后的文件
        '''
        wb2 = Workbook().save(filename2)
        wb1 = load_workbook(filename1)
        wb2 = load_workbook(filename2)
        sheets1 = wb1.get_sheet_names()
        for i in range(len(sheets1)-1):
            wb2.create_sheet()
        sheets2 = wb2.get_sheet_names()
        for index, sheet1 in enumerate(sheets1):
            sheet1 = wb1.get_sheet_by_name(sheet1)
            sheet2 = wb2.get_sheet_by_name(sheets2[index])
            sheet2.title = sheet1.title
            max_row = sheet1.max_row
            max_column = sheet1.max_column
            for m in range(1, max_row + 1):
                # chr(97) = 'a'
                for n in range(97, 97 + max_column):
                    # 转换成ASCII字符
                    n = chr(n)
                    # 单元格编号
                    i = '%s%d' % (n, m)
                    # 获取文件1中该表单的单元格数据
                    cell1 = sheet1[i].value
                    sheet2[i].value = cell1
        wb2.save(filename2)
        wb1.close()
        wb2.close()

    def close(self):
        '''
        操作完excel后，关闭excel文件
        '''
        self.workbook.close()
