import sqlite3
from sweetest.config import db_name, db_initsql
from sweetest.lib.log import logger

class DB(object):
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        sql = open(db_initsql, 'r').read()
        self.cur.executescript(sql)
        self.conn.commit()
        # self.conn.close()

    def insert_result(self, begin_time):
        sql = 'INSERT INTO testresult VALUES (?,?,?,?,?,?,?)'
        t = (None, 0, 0, 0, 0, begin_time, 0)

        self.cur.execute(sql, t)
        self.conn.commit()

    def update_result(self, d):
        '''
        sql1 = 'update testresult set all=' + str(t["testAll"]) +', pass=' + str(t["testPass"]) + \
              ', fail=' + str(t["testFail"]) + ', skip=' + str(t["testSkip"]) + ',total_time=' + t["totalTime"] + \
              ' where id = (select max(id) from testresult)'
        '''

        sql = '''UPDATE testresult SET total= ?, pass= ?, fail= ?, skip= ?, total_time= ? 
        WHERE id = (select max(id) from testresult)'''
        t = (d["testAll"], d["testPass"], d["testFail"], d["testSkip"], d["totalTime"])
        self.cur.execute(sql, t)
        self.conn.commit()

    def insert_suite(self, name):
        sql = 'INSERT INTO testsuite VALUES (?,?,?)'
        t = (None, name, resultID)

        self.cur.execute(sql, t)
        self.conn.commit()


