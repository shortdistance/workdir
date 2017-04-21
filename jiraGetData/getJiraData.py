# -*- coding: utf-8 -*-
 
#mysqldb
import time, MySQLdb

MysqlHost="10.112.103.205"
MysqlUser="jingp"
MysqlPasswd="jingp"
MysqlDB="jiradb"
MysqlCharset="utf8"
conn=MySQLdb.connect(host=MysqlHost,user=MysqlUser,passwd=MysqlPasswd,db=MysqlDB,charset=MysqlCharset)  
cursor = conn.cursor()


n = cursor.execute("select * from sequence")
for row in cursor.fetchall():
	for r in row:
		print r
   
cursor.close()
conn.close()