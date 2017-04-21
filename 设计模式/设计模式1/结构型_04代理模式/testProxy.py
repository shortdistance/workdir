#-*-coding:utf-8-*-

"""
模式特点：为其他对象提供一种代理以控制对这个对象的访问。

程序实例：同模式特点描述。

代码特点：无
"""

class Interface :
    def Request(self):
        pass

class RealSubject(Interface): 
    def Request(self):
        print "Real request."

class Proxy(Interface):
    def Request(self):
        self.real = RealSubject()
        self.real.Request()

if __name__ == "__main__":
    p = Proxy()
    p.Request()