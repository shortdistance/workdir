# -*- coding: utf-8 -*-
 
#mysqldb
import time, MySQLdb
import os
   
#连接
MysqlHost="172.16.9.144"
MysqlUser="vercontrol"
MysqlPasswd="123456"
MysqlDB1="testlink"
MysqlDB2="testlink1"
MysqlCharset="utf8"

conn1=MySQLdb.connect(host=MysqlHost,user=MysqlUser,passwd=MysqlPasswd,db=MysqlDB1,charset=MysqlCharset) 
conn2=MySQLdb.connect(host=MysqlHost,user=MysqlUser,passwd=MysqlPasswd,db=MysqlDB2,charset=MysqlCharset)
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()
#写入
#sql = "insert into user(name,created) values(%s,%s)"   
#param = ("aaa",int(time.time()))
#n = cursor.execute(sql,param)
#print n

#更新
#sql = "update user set name=%s where id=3"   
#param = ("bbb")
#n = cursor.execute(sql,param)
#print n
   
#查询
table1 = []
n = cursor1.execute("show tables;")
print "==================="
for row in cursor1.fetchall():
	for r in row:
		table1.append(r)
		print r

			
			
table2 = []
n = cursor2.execute("show tables;")
print "==================="
for row in cursor2.fetchall():
	for r in row:
		table1.append(r)
		print r
			
		
cursor1.close()
cursor2.close()
conn1.close()
conn2.close()

#os.system('rm -rf /opt/mysql/mysqldata/testlink1')
#os.system('cp -rf /opt/mysql/mysqldata/testlink /opt/mysql/mysqldata/testlink1')
#os.system('chown -R mysql:mysql /opt/mysql/mysqldata/testlink1')
#os.system('chmod -R 755 /opt/mysql/mysqldata/testlink1')