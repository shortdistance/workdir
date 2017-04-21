# -*-coding:utf-8 -*-

import os

if not os.path.exists('data.txt'):
    exit(-1)  # 不存在就退出
lines = open('data.txt').readlines()  # 打开文件，读入每一行
fp = open('data1.txt','w')
for s in lines:
    fp.write(s.replace('"', '&quot;').replace('<', '&lt;').replace('>','&gt;'))
    #.replace('?','&iexcl;')
fp.close()
