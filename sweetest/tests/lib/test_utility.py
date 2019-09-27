import unittest
from sweetest.lib.utility import *
from sweetest.globals import g


class TestUtility(unittest.TestCase):

    def test_data2dict(self):
        data = [['key1', 'key2', 'key3'],
                ['value1-1', 'value2-1', 'value3-1'],
                ['value1-2', 'value2-2', 'value3-2'],
                ['value1-3', 'value2-3', 'value3-3']
                ]
        data1 = [{'key1': 'value1-1', 'key2': 'value2-1', 'key3': 'value3-1'},
                 {'key1': 'value1-2', 'key2': 'value2-2', 'key3': 'value3-2'},
                 {'key1': 'value1-3', 'key2': 'value2-3', 'key3': 'value3-3'}
                 ]
        self.assertEqual(data2dict(data), data1)

    def test_is_number(self):
        s = 1
        self.assertEqual(is_number(s), True)

        s = 1.01
        self.assertEqual(is_number(s), True)

        s = 'a'
        self.assertEqual(is_number(s), False)

    def test_is_operator(self):
        s = '+'
        self.assertEqual(is_operator(s), True)

        s = '-'
        self.assertEqual(is_operator(s), True)

        s = '*'
        self.assertEqual(is_operator(s), True)

        s = '/'
        self.assertEqual(is_operator(s), True)

        s = '%'
        self.assertEqual(is_operator(s), True)

        s = '('
        self.assertEqual(is_operator(s), False)

        s = ')'
        self.assertEqual(is_operator(s), False)

        s = 'a'
        self.assertEqual(is_operator(s), False)

        s = 'a'
        self.assertEqual(is_operator(s), False)

        s = '1'
        self.assertEqual(is_operator(s), False)

    def test_isNotNull(self):
        data = ''
        self.assertEqual(isNotNull(data), False)

        data = None
        self.assertEqual(isNotNull(data), False)

        data = 'ab'
        self.assertEqual(isNotNull(data), True)

    def test_str2int(self):
        s = '1'
        self.assertEqual(str2int(s), 1)

        s = '1,000'
        self.assertEqual(str2int(s), 1000)

        s = '1.0'
        self.assertEqual(str2int(s), 1)

    def test_zero(self):
        s = '1'
        self.assertEqual(zero(s), '1')

        s = '10'
        self.assertEqual(zero(s), '1')

        s = '100'
        self.assertEqual(zero(s), '1')

        s = '100000'
        self.assertEqual(zero(s), '1')

    def test_str2float(self):
        s = '1'
        self.assertEqual(str2float(s), (1.0, 1))

        s = '1.1'
        self.assertEqual(str2float(s), (1.1, 1))

        s = '1.10'
        self.assertEqual(str2float(s), (1.1, 1))

        s = '1000.100000'
        self.assertEqual(str2float(s), (1000.1, 1))

        s = '1,000.100000'
        self.assertEqual(str2float(s), (1000.1, 1))

    def test_json2dict(self):
        j = '{"id": "007", "name": "007", "age": 28, "sex": "male", "phone": "13000000000", "email": "123@qq.com"}'
        d = {'id': '007', 'name': '007', 'age': 28, 'sex': 'male', 'phone': '13000000000', 'email': '123@qq.com'}
        self.assertEqual(json2dict(j), d)

    def test_get_18_string(self):
        self.assertEqual(len(get_18_string()), 18)

        a = get_18_string()
        b = get_18_string()
        self.assertNotEqual(a, b)

    def test_variable2value(self):
        g.var['var1'] = 'test'

        data = '<var1>'
        self.assertEqual(variable2value(data), 'test')
        data = '<var1> by tester!'
        self.assertEqual(variable2value(data), 'test by tester!')

        g.var['var1'] = ['play', 'test']

        data = '<var1>'
        self.assertEqual(variable2value(data), 'play')
        data = '<var1> by tester!'
        self.assertEqual(variable2value(data), 'test by tester!')

        g.var['var1'] = ['play', 'test']

        data = '<var1>'
        self.assertEqual(variable2value(data, 1), ['play', 'test'])

        g.var['var1'] = 1

        data = '<var1>'
        self.assertEqual(variable2value(data), '1')

        g.var['var1'] = [1, 2, 3]

        data = '<var1>'
        self.assertEqual(variable2value(data), '1')
        self.assertEqual(variable2value(data, 1), [2, 3])

    def test_middle2after(self):

        data = '2+3*4-(6/2+5%2)'
        self.assertEqual(middle2after(data), ['2', '3', '4', '*', '+', '6', '2', '/', '5', '2', '%', '+', '-'])

        data = '12+3*4-(1.6/2+15%2)'
        self.assertEqual(middle2after(data), ['12', '3', '4', '*', '+', '1.6', '2', '/', '15', '2', '%', '+', '-'])

        data = '(1+2)*(4-3)'
        self.assertEqual(middle2after(data), ['1', '2', '+', '4', '3', '-', '*'])

        data = '(1+2)*((4-3)+(8-6))'
        self.assertEqual(middle2after(data), ['1', '2', '+', '4', '3', '-', '8', '6', '-', '+', '*'])

        data = 'values(2+3*4)'
        self.assertEqual(middle2after(data), ['v', 'a', 'l', 'u', 'e', 's', '2', '3', '4', '*', '+'])

    def test_expression2value(self):
        l = ['2', '3', '4', '*', '+', '6', '2', '/', '5', '2', '%', '+', '-']
        self.assertEqual(expression2value(l), '10.0')

        l = ['12', '3', '4', '*', '+', '1.6', '2', '/', '15', '2', '%', '+', '-']
        self.assertEqual(expression2value(l), '22.2')

        l = ['1', '2', '+', '4', '3', '-', '*']
        self.assertEqual(expression2value(l), '3')

        l = ['1', '2', '+', '4', '3', '-', '8', '6', '-', '+', '*']
        self.assertEqual(expression2value(l), '9')

        l = ['v', 'a', 'l', 'u', 'e', 's', '2', '3', '4', '*', '+']
        self.assertEqual(expression2value(l), 'values14')

    def test_replace(self):
        g.var['var1'] = 'test'

        data = '<var1>'
        self.assertEqual(replace(data), 'test')

        data = 'A <var1> is running!'
        self.assertEqual(replace(data), 'A test is running!')

        g.var['num1'] = [10, 20]
        g.var['num2'] = [2, 4]

        data = '<num1>+<num2>'
        self.assertEqual(replace(data), '12')

        data = '<num1>-<num2>'
        self.assertEqual(replace(data), '16')

        g.var['num1'] = [1, 1.6]
        g.var['num2'] = [3, 12]

        data = '(<num1>+2)*((4-<num2>)+(8-6))'
        self.assertEqual(replace(data), '9')

        data = '<num2>+3*4-(<num1>/2+15%2)'
        self.assertEqual(replace(data), '22.2')

        data = 'https:\/\/im.dingtalk.com\/'
        self.assertEqual(replace(data), 'https://im.dingtalk.com/')

    def test_replace_list(self):
        g.var['var1'] = 'test'

        data = ['<var1>']
        replace_list(data)
        self.assertEqual(data, ['test'])

        data = ['<var1>', 'A <var1> is running!']
        replace_list(data)
        self.assertEqual(data, ['test', 'A test is running!'])

        g.var['num1'] = [10, 20]
        g.var['num2'] = [2, 4]
        data = ['<num1>+<num2>', '<num1>-<num2>']
        replace_list(data)
        self.assertEqual(data, ['12', '16'])

        g.var['num1'] = [1, 1.6]
        g.var['num2'] = [3, 12]
        data = ['(<num1>+2)*((4-<num2>)+(8-6))', '<num2>+3*4-(<num1>/2+15%2)', 'https:\/\/im.dingtalk.com\/']
        replace_list(data)
        self.assertEqual(data, ['9', '22.2', 'https://im.dingtalk.com/'])

    def test_replace_dict(self):
        g.var['var1'] = 'test'

        data = {'key1': '<var1>'}
        replace_dict(data)
        self.assertEqual(data, {'key1': 'test'})

        data = {'key1': '<var1>', 'key2': 'A <var1> is running!'}
        replace_dict(data)
        self.assertEqual(data, {'key1': 'test', 'key2': 'A test is running!'})

        g.var['num1'] = [10, 20]
        g.var['num2'] = [2, 4]
        data = {'key1': '<num1>+<num2>', 'key2': '<num1>-<num2>'}
        replace_dict(data)
        self.assertEqual(data, {'key1': '12', 'key2': '16'})

        g.var['num1'] = [1, 1.6]
        g.var['num2'] = [3, 12]
        data = {'key1': '(<num1>+2)*((4-<num2>)+(8-6))', 'key2': '<num2>+3*4-(<num1>/2+15%2)', 'key3': 'https:\/\/im.dingtalk.com\/'}
        replace_dict(data)
        self.assertEqual(data, {'key1': '9', 'key2': '22.2', 'key3': 'https://im.dingtalk.com/'})

        g.var['num1'] = ['2019-09-30', '2019-10-01', '2019-10-02']
        data = {'key1': '<num1>', 'datatype': 'y'}
        replace_dict(data)
        self.assertEqual(data, {'key1': ['2019-09-30', '2019-10-01', '2019-10-02'], 'datatype': 'y'})


if __name__ == '__main__':
    unittest.main()
