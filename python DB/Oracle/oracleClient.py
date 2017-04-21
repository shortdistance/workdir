__author__ = 'Raychang'
# -*- coding:utf-8 -*-
from config import *
import cx_Oracle
import sys


def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    if defaultType in (cx_Oracle.STRING, cx_Oracle.FIXED_CHAR):
        return cursor.var(unicode, size, cursor.arraysize)

class FileOper:
    def __init__(self, filePath):
        self.f = None
        try:
            self.f = open(filePath, 'w')
        except Exception, e:
            print u'路径不合法!!'
            sys.exit(-1)

    def writeFile(self, line):
        if self.f:
            self.f.write(line)
            self.f.flush()

    def close(self):
        if self.f:
            self.f.close()


class OracleOper:
    def __init__(self):
        self.cur = None
        self.con = cx_Oracle.connect(DBLinkString)
        self.con.outputtypehandler = OutputTypeHandler
        if self.con:
            print u'连接成功!!'
        else:
            print u'连接失败!!'
            sys.exit(-1)

    def showVersion(self):
        if self.con:
            print self.con.version

    def query(self, sqlStr):
        self.cur = self.con.cursor()
        self.cur.execute(sqlStr)

        myfile = FileOper(filePathTemp)
        self.cur.arraysize = 100000

        for row in self.cur.fetchmany():
            temprow = ''
            for i in range(len(row)):
                if i == 0:
                    if len(row) > 1:
                        temprow = str(row[i]) + ','
                    else:
                        temprow = str(row[i])
                elif len(row) > 1 and i == len(row) - 1:
                    temprow = temprow + str(row[i])
                else:
                    temprow = temprow + str(row[i]) + ','

            print temprow
            myfile.writeFile(temprow + '\n')
        myfile.close()

    def dbDisConn(self):
        if self.con:
            self.con.close()


if __name__ == '__main__':
    mydb = OracleOper()
    mydb.showVersion()
    mydb.query(sqlTemp)
    mydb.dbDisConn()

