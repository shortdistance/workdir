#-*- coding:utf-8 -*-
__author__ = 'Raychang'


import svn.remote

r = svn.remote.RemoteClient('http://172.16.9.106:9001/svn/qmd/tools', username='zhangleid', password='1qaz2wsx')
ret = r.log_default()
