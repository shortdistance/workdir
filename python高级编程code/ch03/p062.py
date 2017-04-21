class BaseBase(object):
    def __init__(self):
        print 'basebase'
        super(BaseBase, self).__init__()         

class Base1(BaseBase):
    def __init__(self):
        print 'base1'
        super(Base1, self).__init__()         

class Base2(BaseBase):
    def __init__(self, arg):
        print 'base2'
        super(Base2, self).__init__()         

class MyClass(Base1 , Base2):
    def __init__(self, arg):
        print 'my base'
        super(MyClass, self).__init__()

m = MyClass(10)
