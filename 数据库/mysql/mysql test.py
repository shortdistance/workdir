# -*- coding: utf-8 -*-
 
#mysqldb
import time, MySQLdb
   
   #����
MysqlHost="172.16.9.144"
MysqlUser="vercontrol"
MysqlPasswd="123456"
MysqlDB="vercontrol"
MysqlCharset="utf8"
conn=MySQLdb.connect(host=MysqlHost,user=MysqlUser,passwd=MysqlPasswd,db=MysqlDB,charset=MysqlCharset)  
cursor = conn.cursor()

   #д��
#sql = "insert into user(name,created) values(%s,%s)"   
#param = ("aaa",int(time.time()))
#n = cursor.execute(sql,param)
#print n

   #����
#sql = "update user set name=%s where id=3"   
#param = ("bbb")
#n = cursor.execute(sql,param)
#print n
   
   #��ѯ
n = cursor.execute("select * from vc_account")
for row in cursor.fetchall():
	for r in row:
		print r
   
   #ɾ��
#sql = "delete from user where name=%s"   
#param =("aaa")
#n = cursor.execute(sql,param)
#print n

cursor.close()
   #�ر�
conn.close()