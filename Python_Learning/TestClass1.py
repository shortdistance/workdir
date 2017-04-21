#coding=gbk

class ren:
    def __init__ (self, name='zhangsan', age=10, salary = 100):
        self.name = name
        self.age = age
        self.__salary = salary

    def __str__ (self):
        return 'haha __str__'
        
    
    def getName (self):
        return self.name
    def getAge (self):
        return self.age
    
    def setName (self, name):
        self.name = name
    
    def sefAge (self, age):
        self.age = age
    
    def getSalary (self):
        self.__printSalary()
        return self.__salary
    
    def __printSalary (self):   #私有方法
        print self.__salary
    
    def setSalary (self, salary):
        if type(salary) ==int and salary > 0:
            self.__salary = salary
        else:
            print 'param is invalid!!'
    
    @classmethod
    def run (self):             #类方法
        print 'hello'
        
    @staticmethod
    def r1 ():                  #静态方法
        print 'world'
        

if __name__ == '__main__':
    r1 = ren('zhanglei',32)
    print r1.name
    print r1.age
    r1.getSalary()
    r1.setSalary(1)
    print r1.getSalary()
    ren.run()
    ren.r1()
    print r1