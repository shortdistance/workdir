# -*-coding:utf-8 -*-

__author__ = 'raychang'


class Staff:
    def __init__(self, no, name, position, salary):
        self.no = no
        self.name = name
        self.position = position
        self.salary = salary

        self.length = 0
        self.length += len(self.no) if self.no and self.no.strip() else 0
        self.length += len(self.name) if self.name and self.name.strip() else 0
        self.length += len(self.position) if self.position and self.position.strip() else 0
        self.length += len(str(self.salary)) if str(self.salary) and str(self.salary).strip() else 0

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

    def accept(self, visitor):
        pass


class Manager(Staff):
    def __init__(self, no, name, position, salary):
        Staff.__init__(self, no, name, position, salary)
        self.arrayList = []

    def add(self, staff):
        if staff and staff not in self.arrayList:
            self.arrayList.append(staff)

    def remove(self, no):
        staff = None
        if no and no.strip():
            for x in self.arrayList:
                if x and x.no == no:
                    staff = x
                    self.arrayList.remove(x)

        return staff

    def accept(self, visitor):
        visitor.visitManager(self)
        for x in self.arrayList:
            if x:
                x.accept(visitor)


class Employees(Staff):
    def __init__(self, no, name, position, salary):
        Staff.__init__(self, no, name, position, salary)

    def add(self, staff):
        return

    def remove(self, no):
        return None

    def accept(self, visitor):
        visitor.visitEmployee(self)


class IVisitor:
    def visitManager(self, manager):
        pass

    def visitEmployee(self, employee):
        pass


class BaseInfoVisitor(IVisitor):
    def visitManager(self, manager):
        print u'- 管理者：',
        manager.printUserBaseInfo()

    def visitEmployee(self, employee):
        print u'- 一般员工：',
        employee.printUserBaseInfo()


if __name__ == '__main__':
    boss = Manager('1', u'大老板', u'CEO', 100000)
    financeManager = Manager('11', u'张总', u'财务部经理', 60000)
    personnelManager = Manager('12', u'王总', u'人事部经理', 60000)
    technicalManager = Manager('13', u'陈总', u'技术部经理', 60000)

    tech_dept_assistant = Manager('1301', u'王助理', u'部门助理', 20000)
    tech_dept_manager1 = Manager('1302', u'主管1', u'技术主管', 30000)

    softwareEngineer1 = Employees('1302001', u'张三', u'软件工程师', 5000)
    softwareEngineer2 = Employees('1302002', u'李四', u'软件工程师', 5000)
    softwareEngineer3 = Employees('1302003', u'王五', u'软件工程师', 5000)

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

    boss.accept(BaseInfoVisitor())
