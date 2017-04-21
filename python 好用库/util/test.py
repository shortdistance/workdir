#-*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from path import path
d = path('D:\\Users')
'''
for f in d.files('*.py'):
    print f.abspath()
for dir in d.walkdirs():
    for f in dir.files('*.py'):
        print f.abspath()

'''

for f in d.walkfiles('*.py'):
    print f.abspath()