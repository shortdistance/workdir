class BaseBase(object):
    def __init__(self, *args, **kw):
        print 'basebase'
        super(BaseBase, self).__init__(*args, **kw) 

class Base1(BaseBase):
    def __init__(self, *args, **kw):
        print 'base1'
        super(Base1, self).__init__(*args, **kw)         

class Base2(BaseBase):
    def __init__(self, arg, *args, **kw):
        print 'base2'
        super(Base2, self).__init__(*args, **kw) 

class MyClass(Base1 , Base2):
    def __init__(self, arg):
        print 'my base'
        super(MyClass, self).__init__(arg)

m = MyClass(10)
