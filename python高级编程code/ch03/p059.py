class BaseBase(object):
    def method(self):
        print 'BaseBase'

class Base1(BaseBase):
    pass

class Base2(BaseBase):
    def method(self):
        print 'Base2'

class MyClass(Base1, Base2):
    pass

here = MyClass()
here.method()

def L(klass):
    return [k.__name__ for k in klass.__mro__]

#L[MyClass(Base1, Base2)] = MyClass + merge(L[Base1], L[Base2], Base1, Base2)
       
print L(MyClass)
