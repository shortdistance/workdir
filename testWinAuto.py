#-*- coding:utf-8 -*-


from pywinauto import application 
from pywinauto import findwindows

path = u'D:\\Program Files (x86)\\医院管理系统\\main.exe'

app = application.Application
app.start(path)

pid = findwindows.find_windows(title=u'系统登录')[0]

