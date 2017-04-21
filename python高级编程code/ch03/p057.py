class Base1: 
    pass 

class Base2: 
    def method(self): 
        print 'Base2' 

class MyClass(Base1, Base2): 
    pass 

here = MyClass() 
here.method() 
