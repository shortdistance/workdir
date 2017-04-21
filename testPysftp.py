#-*- coding:utf-8 -*-
import pysftp
import sys

 
srv = pysftp.Connection(host="172.16.9.144", 
                        username="developer",
                        password="123456")

srv.cd('~')
print srv.pwd
print srv.execute('ls -l')

srv.get('/home/developer/test.db','d:\\test.db')

srv.put(u'C:\\Users\\raychang\\Desktop\\需要看.txt',u'/home/developer/需要看.txt')