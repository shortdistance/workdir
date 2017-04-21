class MyClass(object):
    def __new__(cls):
        print '__new__ called'
        return object.__new__(cls) 
# default factory
    def __init__(self):
        print '__init__ called'
        self.a = 1

instance = MyClass()

class MyOtherClassWithoutAConstructor(MyClass):
    pass

instance = MyOtherClassWithoutAConstructor()

class MyOtherClass(MyClass):
    def __init__(self):
        print 'MyOther class __init__ called'
        super(MyOtherClass, self).__init__()
        self.b = 2

instance = MyOtherClass()
