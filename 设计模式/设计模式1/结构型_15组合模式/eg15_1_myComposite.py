#-*- coding:utf-8 -*-
__author__ = 'raychang'


class Employee:
    def __init__(self, no, name, position, salary):
        self.no = no
        self.name = name
        self.position = position
        self.salary = salary

    def printUserBaseInfo(self):
        print u'|%s %s  %s  %s' % (self.no, self.name, self.position, self.salary)

    def getNo(self):
        return self.no

    def setNo(self, no):
        self.no = no

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary


class Manager:
    def __init__(self, no, name, position, salary):
        self.no = no
        self.name = name
        self.position = position
        self.salary = salary
        self.arrayList = []
        self.length = 0

        self.length += len(self.no) if self.no and self.no.strip() else 0
        self.length += len(self.name) if self.name and self.name.strip() else 0
        self.length += len(self.position) if self.position and self.position.strip() else 0
        self.length += len(str(self.salary)) if str(self.salary) and str(self.salary).strip() else 0

    def printUserBaseInfo(self):
        print u'|%s %s  %s  %s' % (self.no, self.name, self.position, self.salary)

    def add(self, obj):
        if isinstance(obj, Manager) or isinstance(obj, Employee):
            self.arrayList.append(obj)

    def printChar(self, layer):
        print '-' * (2 * layer),

    def printEmployeesInfo(self, layer):
        tmpLayer = layer + 1
        for i in self.arrayList:
            if isinstance(i, Employee):
                self.printChar(tmpLayer)
                i.printUserBaseInfo()

            if isinstance(i, Manager):
                self.printChar(tmpLayer)
                i.printUserBaseInfo()
                i.printEmployeesInfo(tmpLayer)

    def getNo(self):
        return self.no

    def setNo(self, no):
        self.no = no

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

    def getArrayList(self):
        return self.arrayList

    def setArrayList(self, arraylist):
        self.arrayList = arraylist


if __name__ == '__main__':
    boss = Manager('1', u'大老板', u'CEO', 100000)
    financeManager = Manager('11', u'张总', u'财务部经理', 60000)
    personnelManager = Manager('12', u'王总', u'人事部经理', 60000)
    technicalManager = Manager('13', u'陈总', u'技术部经理', 60000)

    tech_dept_assistant = Manager('1301', u'王助理', u'部门助理', 20000)
    tech_dept_manager1 = Manager('1302', u'主管1', u'技术主管', 30000)

    softwareEngineer1 = Employee('1302001', u'张三', u'软件工程师', 5000)
    softwareEngineer2 = Employee('1302002', u'李四', u'软件工程师', 5000)
    softwareEngineer3 = Employee('1302003', u'王五', u'软件工程师', 5000)

    tech_dept_manager1.add(softwareEngineer1)
    tech_dept_manager1.add(softwareEngineer2)
    tech_dept_manager1.add(softwareEngineer3)

    tech_dept_manager2 = Manager('1303', u'主管2', u'技术主管', 30000)

    technicalManager.add(tech_dept_assistant)
    technicalManager.add(tech_dept_manager1)
    technicalManager.add(tech_dept_manager2)

    marketlManager = Manager('14', u'吴总', u'市场部经理', 60000)

    boss.add(financeManager)
    boss.add(personnelManager)
    boss.add(technicalManager)
    boss.add(marketlManager)

    boss.printUserBaseInfo()
    boss.printEmployeesInfo(1)
