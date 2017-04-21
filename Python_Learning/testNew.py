#-*-coding:utf-8-*-
import new
import string
class Sample:
    a = "default"
    def __init__(self):
        self.a = "initialised"

    def __repr__(self):
        return self.a
#
# create instances
a = Sample()
print "normal", "=>", a

b = new.instance(Sample, {})
print "new.instance", "=>", b
b.__init__()
print "after __init__", "=>", b
c = new.instance(Sample, {"a": "assigned"})
print "new.instance w. dictionary", "=>", c

class a:
    def __init__ (self):
        self.name ='zl'
        self.age =30
    def __repr__ (self):
        return self.name
        
    pass
    
str1 = new.instance(a,{})
str1.__init__()
print str1