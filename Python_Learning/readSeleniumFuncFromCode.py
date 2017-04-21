#-*- coding:utf-8 -*-
'''
import Selenium2Library
for item in dir(Selenium2Library):
    if item[0]=='_' and item[1]!='_':
        f = open('C:\\%s.txt' % item, 'r')
        records = f.readlines()
        f.close()
        
        f1 = open('C:\\%s.txt' % item, 'w')
        for i in range(len(records)):
            pureLine = ' '.join(records[i].split('\n')[0].split('_'))
            f1.write('%s\n'% pureLine)
        f1.close()
        
'''

from selenium import webdriver
import sys

proxy = sys.modules['selenium.webdriver'].Proxy()
print proxy