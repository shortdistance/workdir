class BaseBase: 
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
