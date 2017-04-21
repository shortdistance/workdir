#-*-coding:utf-8 -*-
"""
模式特点：将一个类的接口转换成为客户希望的另外一个接口。

程序实例：用户通过适配器使用一个类的方法。

代码特点：无
"""


class Target:
    def Request():
        print "common request."

class Adaptee(Target):
    def SpecificRequest(self):
        print "specific request."

class Adapter(Target):
    def __init__(self,ada):
        self.adaptee = ada
    def Request(self):
        self.adaptee.SpecificRequest()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()