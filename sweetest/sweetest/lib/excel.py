import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font, colors
from openpyxl.styles.fills import PatternFill


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

    def write(self, testsuite, sheet_name, filename):
        '''
        将测试结果写入excel报告中，并进行格式化
        :param testsuite: 测试用例集
        :param sheet_name: 表单名
        :param filename: 文件名
        '''
        sheet = self.workbook.get_sheet_by_name(sheet_name)
        for cell in sheet[1]:
            cell.fill = DarkRedFill
            cell.font = Font(color=colors.WHITE)
        m = 0
        n = 2
        while n < (sheet.max_row + 1):
            self.length = 0
            i = '%s%d' % (chr(97), n)
            # 单元格数据
            # cell = sheet[i].value, ''

            j = '%s%d' % (chr(111), n)
            sheet[j].value = testsuite[m].get('result', '')
            if sheet[j].value:
                sheet[j].fill = Fills[sheet[j].value]
                sheet[j].font = Font(color=colors.WHITE)
            for index, step in enumerate(testsuite[m].get('steps')):
                    k = '%s%d' % (chr(110), (n+index))
                    l = '%s%d' % (chr(112), (n+index))
                    sheet[k].value = step.get('score', '')
                    sheet[k].font = Font(color=colors.BLACK)
                    if sheet[k].value == 'NO':
                        sheet[k].fill = GrayFill
                        sheet[k].font = Font(color=colors.WHITE)
                    sheet[l].value = step.get('remark', '')
                    sheet[l].font = Font(color=colors.BLACK)
                    self.length += 1
            m = m+1
            n = n+self.length

        self.workbook.save(filename)

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
