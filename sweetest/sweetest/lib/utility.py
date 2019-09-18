import re
import json
from sweetest.config import header
from sweetest.globals import g
from sweetest.config import addition, subtraction, multiplication, division, residual, lparenthesis, rparenthesis, lbrackets, rbrackets
from selenium.webdriver.common.keys import Keys
from sweetest.lib.log import logger


def data2dict(data):
    '''
    把带头标题的二元数组，转换成以标题为 key 的 dict  的 list
    用于解析元素、解析用例
    :param data: 带头标题的二元数组（元素表、用例表）
    :return: 以标题为 key 的 dict  的 list（元素表、用例表）
    '''

    list_dict_data = []
    key = []
    # 第一行为头标题，先获取所有的头标题，存储在key列表中
    for d in data[0]:
        k = d.strip()
        # 解析时，如果为中文，则替换成英文
        h = header.get(k, k).lower()
        key.append(h)
    # 遍历其余行，进行结构转换
    for d in data[1:]:
        dict_data = {}
        for i in range(len(key)):
            if isinstance(d[i], str):
                dict_data[key[i]] = str(d[i]).strip()
            else:
                dict_data[key[i]] = d[i]
        list_dict_data.append(dict_data)
    return list_dict_data


def is_number(s):
    '''
    检测值是否是数字
    :param s: 数据
    :return: 输入是数字，则返回True；否则返回False
    '''

    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def replace_dict(data):
    '''
    对dict的变量进行值替换
    :param data: dict结构的数据，带变量
    '''

    for key in data:
        data[key] = replace(data[key])


def replace_list(data):
    '''
    对list的变量进行值替换
    :param data: list结构的数据，带变量
    '''

    for i in range(len(data)):
        data[i] = replace(data[i])


def replace(data):
    '''
    对输入进行变量替换、表达式计算
    :param data: 测试数据/预期结果/输出数据
    :return: 替换变量、进行运算后的值
    '''

    # 数据中的转义字符先替换成特定字符
    new_data = data.replace('\\+', addition).replace('\\-', subtraction).replace('\\*', multiplication).\
        replace('\\/', division).replace('\\%', residual).replace('\\(', lparenthesis).replace('\\)', rparenthesis).\
        replace('\\<', lbrackets).replace('\\>', rbrackets)

    # 将数据中的变量替换为具体的值
    new_data = variable2value(new_data)

    # 带有运算符，则进行表达式运算
    if '+' in new_data or '-' in new_data or '*' in new_data or '/' in new_data or '%' in new_data:
        expression = middle2after(new_data)
        value = (''.join([str(x) for x in expression]))
        if new_data != value:
            new_data = str(expression2value(expression))

    # 恢复原先的转义字符
    if isinstance(new_data, str):
        new_data = new_data.replace(addition, '+').replace(subtraction, '-').replace(multiplication, '*').\
            replace(division, '/').replace(residual, '%').replace(lparenthesis, '(').replace(rparenthesis, ')').\
            replace(lbrackets, '<').replace(rbrackets, '>')

    return new_data


def variable2value(data):
    '''
    对数据中的变量进行值替换
    :param data: 带有变量的数据，变量用<>括起来
    :return: 替换变量后的值
    '''

    # <>内的变量替换成具体值
    # 正则匹配出 data 中所有 <> 中的变量，返回列表
    keys = re.findall(r'<(.*?)>', data)

    for i, k in enumerate(keys):
        if k in g.var:
            # 如果在 g.var 中是 list，则 pop 第一个值
            if isinstance(g.var[k], list):
                value = g.var[k].pop(0)
                # 再判断一下此 list 是否只有一个值了，如果是，则从 list 变为该值
                if len(g.var[k]) == 1:
                    g.var[k] = g.var[k][0]
            # 如果在 g.var 中是值，则直接赋值
            else:
                value = g.var[k]
            data = data.replace('<' + k + '>', str(value))
        # 键盘操作
        elif data == '<'+k+'>' and 'Keys.' in k:
            data = eval(k)

    return data


def middle2after(data):
    '''
    中缀表达式转换为后缀表达式
    中缀表达式: 2+3×4             后缀表达式：234×+
    中缀表达式: 3×(2+3)           后缀表达式：323+×
    中缀表达式: values(2+3×4)     后缀表达式：values234×+
    :param data: 中缀表达式
    :return: 后缀表达式
    '''

    # 运算符的优先级，数字越大，优先级越高
    ops_pri = {
        '(': 3,
        ')': 3,
        '*': 2,
        '/': 2,
        '%': 2,
        '+': 1,
        '-': 1
    }

    expression = []
    ops = []
    # 遍历每个字符
    for i, s in enumerate(data):
        # 若字符是运算符, 且运算符左边的字符是数字、右边的字符是数字或左括号
        if s in ['+', '-', '*', '/', '%'] and (i > 0) and (is_number(data[i-1]) and (is_number(data[i+1]) or data[i+1]=='(')):
            while len(ops) >= 0:
                # 运算符栈为空，则运算符直接放入
                if len(ops) == 0:
                    ops.append(s)
                    break
                # 运算符栈非空，比较优先级
                op = ops.pop()
                # 在括号内或优先级高，则入运算符栈
                if op == '(' or ops_pri[s] > ops_pri[op]:
                    ops.append(op)
                    ops.append(s)
                    break
                # 否则入表达式栈
                else:
                    expression.append(op)
        # 左括号，直接入运算符栈
        elif s == '(' and (i > 0) and (is_number(data[i-1]) and is_number(data[i+1])):
            ops.append(s)
        # 右括号，循环出运算符栈、入表达式栈，直到遇左括号为止
        elif s == ')' and (i > 0) and (is_number(data[i-1]) and is_number(data[i+1])):
            while len(ops) > 0:
                op = ops.pop()
                if op == '(':
                    break
                else:
                    expression.append(op)
        # 数值或无需做运算的计算符，直接入表达式栈
        else:
            value = s
            if i > 0 and (is_number(s) or s == '.'):
                j = i-1
                while j >= 0:
                    if not is_number(data[j]) and (data[j]!='.'):
                        break
                    if not is_number(data[j:i+1]):
                        break
                    j = j-1
                value = data[j+1:i+1]
                if j+1 != i:
                    expression.pop()
            expression.append(value)

    # 若运算符栈还有值，直接入表达式栈
    while len(ops) > 0:
        expression.append(ops.pop())

    return expression


def expression2value(expression):
    '''
    执行运算表达式
    :param expression: 运算表达式
    :return: 执行运算后的数据
    '''

    value = []
    for s in expression:
        # 运算符
        if s in ['+', '-', '*', '/', '%']:
            v1, v2 = '', ''
            # 运算符右边的字符
            if value:
                v2 = value.pop()
            # 运算符左边的字符
            if value:
                v1 = value.pop()
            # 若运算符左、右两边都是数字，则执行运算
            if is_number(v1) and is_number(v2):
                result = eval(str(v1) + s + str(v2))
                # 运算结果入栈
                value.append(result)
            # 若运算符左或右边字符非数字，则不执行运算，直接入栈
            else:
                value.append(v1)
                value.append(v2)
                value.append(s)
        # 非运算符，直接入栈
        else:
            value.append(s)
    # 各值拼接成字符串
    value = (''.join([str(x) for x in value]))

    return value


def isNotNull(content):
    '''
    检测输入是否为空
    :param content: 输入内容
    :return: 输入非空，返回True，否则返回False
    '''

    if content and content.strip():
        return True
    else:
        return False


def str2int(s):
    '''
    类型转换，字符串转INT
    :param s: 字符串
    :return: INT数值
    '''

    s = s.replace(',', '').split('.', 1)
    if len(s) == 2:
        dot = s[-1]
        assert int(dot) == 0
    return int(s[0])


def zero(s):
    '''
    去掉右边的0
    :param s: 输入
    :return: 去掉右边0后的数据
    '''
    if s and s[-1] == '0':
        s = s[:-1]
        s = zero(s)
    return s


def str2float(s):
    '''
    类型转换，字符串转Float
    :param s: 字符串
    :return: Float数值
    '''

    s = str(s).replace(',', '').split('.', 1)
    dot = '0'
    if len(s) == 2:
        dot = s[-1]
        dot = zero(dot)
    f = float(s[0]+ '.' +dot)

    return round(f, len(dot)), len(dot)


def json2dict(s):
    '''
    类型转换，json转dict
    :param s: json
    :return: dict
    '''

    s = str(s)
    d = {}
    try:
        d = json.loads(s)
    except:
        try:
            d = eval(s)
        except:
            s = s.replace('true', 'True').replace('false', 'False').replace('null', 'None').replace('none', 'None')
            d = eval(s)
    return d


def get_18_string():
    """随机获取 18 位字符串"""
    return uuid.uuid4().hex[:18]

