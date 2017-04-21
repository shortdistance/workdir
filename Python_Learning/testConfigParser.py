#-*- coding:utf-8 -*-
import ConfigParser

'''
conf = ConfigParser.ConfigParser()
conf.add_section('Mysql')
conf.set('Mysql','user','vercontrol')
conf.set('Mysql','passwd', '123456')
conf.set('Mysql','host','172.16.9.144')
conf.set('Mysql','port','3306')

f = open('C:\\Users\\raychang\\Desktop\\conf.ini','wb')
conf.write(f)
f.close()

print conf.get('Mysql','port')
print conf.items('Mysql')
'''
conf = ConfigParser.ConfigParser()
conf.read('C:\\Users\\raychang\\Desktop\\conf.ini')
print conf.get('db1', 'conn_str')
print conf.get('db2', 'conn_str')

'''
[DEFAULT]
conn_str = %(dbn)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s
dbn = mysql
user = root
host=localhost
port = 3306
[db1]
user = aaa
pw=ppp
db=example
[db2]
host=192.168.0.110
pw=www
db=example

'''