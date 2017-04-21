# -*- coding: utf-8 -*-
 
#mysqldb
import time, MySQLdb
   
   #连接
MysqlHost="172.16.9.144"
MysqlUser="vercontrol"
MysqlPasswd="123456"
MysqlDB="vercontrol"
MysqlCharset="utf8"
conn=MySQLdb.connect(host=MysqlHost,user=MysqlUser,passwd=MysqlPasswd,db=MysqlDB,charset=MysqlCharset)  
cursor = conn.cursor()

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
n = cursor.execute("select * from vc_account")
for row in cursor.fetchall():
	for r in row:
		print r
   
   #删除
#sql = "delete from user where name=%s"   
#param =("aaa")
#n = cursor.execute(sql,param)
#print n

cursor.close()
   #关闭
conn.close()