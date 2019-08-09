from sweetest.globals import g
from pathlib import Path
import json
import pdfkit
from pdf2image import convert_from_path
from sweetest.lib.log import logger


def htmlreport():
    '''
    输出html报告
    '''
    # 读取html模板内容
    with open(g.html_template, 'rb') as file1:
        body = file1.readlines()
    with open(g.htmlreport_file, 'wb') as file2:
        # 循环遍历，对变量进行值替换
        for item in body:
            if item.strip().startswith(b'var resultData'):
                head = '    var resultData = '
                item = item.decode().split(head)
                item[1] = head + json.dumps(g.results, ensure_ascii=False, indent=4)
                item = ''.join(item).encode()
                item = bytes(item) + b';\n'
            # 写入html报告文件中
            file2.write(item)
    html2img()


def html2img():
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    try:
        pdfkit.from_file(str(g.htmlreport_file), str(Path('htmlreport') / f'pdf.pdf'), options=options)
        pages = convert_from_path(Path('htmlreport') / f'pdf.pdf')
        for i in range(0, len(pages)):
            pages[i].save(Path('htmlreport') / f'image{i+1}.png', 'PNG')
    except:
        logger.error("测试未执行！请检查测试配置是否正确！" + "\r\n")

