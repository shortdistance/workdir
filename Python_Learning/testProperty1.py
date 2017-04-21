#-*- coding:utf-8 -*-

class A(object):
    _value = 0
    def __init__(self):
        self._value = 0
    
    @property
    def x(self):
        return self._value
    
    @x.setter
    def x(self, value):
        self._value = value
    
    @x.deleter
    def x(self):
        del self._value
    
    
obj = A()
obj.x = 10
print obj.x + 2
del obj.x