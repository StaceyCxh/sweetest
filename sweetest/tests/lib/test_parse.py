import unittest, os
from sweetest.lib.parse import *
from sweetest.globals import g
from sweetest.config import all_keywords


class TestParse(unittest.TestCase):

    def test_check_keyword(self):
        kw = '打开'
        self.assertEqual(check_keyword(kw), 'OPEN')

        kw = 'OPEN'
        self.assertEqual(check_keyword(kw), 'OPEN')

        kw = '执行'
        self.assertEqual(check_keyword(kw), 'EXECUTE')

        kw = 'EXECUTE'
        self.assertEqual(check_keyword(kw), 'EXECUTE')

        kw = 'OPTIONS'
        self.assertEqual(check_keyword(kw), 'OPTIONS')

        kw = '按键码'
        self.assertEqual(check_keyword(kw), 'PRESS_KEYCODE')

        kw = 'PRESS_KEYCODE'
        self.assertEqual(check_keyword(kw), 'PRESS_KEYCODE')

        kw = '使用'
        self.assertEqual(check_keyword(kw), None)

    def test_analyze_record(self):
        record = {}
        data = [['key1', 'key2', 'key3'], ['value1', 'value2', 'value3'], ['value12', 'value22', 'value33']]
        d = ['value1', 'value2', 'value3']
        self.assertEqual(analyze_record(record, data, d, 2), {'key3': 'value3'})

        record = {'key3': 'value3'}
        d = ['value12', 'value22', 'value33']
        self.assertEqual(analyze_record(record, data, d, 2), {'key3': ['value3', 'value33']})

    def test_read_record(self):
        data_file = os.path.abspath('../../data/Baidu-baidu.csv')
        result = {'_keywords': ['segmentfault', '豆瓣'],
                  '_title': ['SegmentFault 思否', '豆瓣']
                  }
        self.assertEqual(read_record(data_file), result)

        data_file = os.path.abspath('../../data/Baidu-baidu1.csv')
        data = [['_keywords', '_title', 'flag'],
                ['segmentfault', 'SegmentFault 思否', ''],
                ['豆瓣', '豆瓣', '']
                ]
        write_csv(data_file, data, encoding='utf-8')
        result = {'_keywords': 'segmentfault',
                  '_title': 'SegmentFault 思否'
                  }
        self.assertEqual(read_record(data_file), result)
        data = read_csv(data_file, encoding='utf-8')
        data1 = [['_keywords', '_title', 'flag'],
                ['segmentfault', 'SegmentFault 思否', 'Y'],
                ['豆瓣', '豆瓣', '']
                ]
        self.assertEqual(data, data1)

        data_file = os.path.abspath('../../data/Baidu-baidu2.csv')
        data = [['_keywords', '_title', 'flag'],
                ['segmentfault', 'SegmentFault 思否', 'Y'],
                ['豆瓣', '豆瓣', '']
                ]
        write_csv(data_file, data, encoding='utf-8')
        result = {'_keywords': '豆瓣',
                  '_title': '豆瓣'
                  }
        self.assertEqual(read_record(data_file), result)
        data = read_csv(data_file, encoding='utf-8')
        data1 = [['_keywords', '_title', 'flag'],
                ['segmentfault', 'SegmentFault 思否', 'Y'],
                ['豆瓣', '豆瓣', 'Y']
                ]
        self.assertEqual(data, data1)



if __name__ == '__main__':
    unittest.main()