#-*- coding:utf-8 -*-

class A(object):
    def __init__(self):
        self._value = 0
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value
        
    def del_attr(self):
        del self._value
        
    x = property(get_value, set_value, del_attr)
    
    
obj = A()
obj.x = 10
print obj.x + 2
del obj.x
