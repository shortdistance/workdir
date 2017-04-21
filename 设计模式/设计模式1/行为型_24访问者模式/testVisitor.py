# -*-coding:utf-8-*-
"""
"""


# -*- coding: UTF-8 -*-
class Person:
    def Accept(self, visitor):
        pass


class Man(Person):
    def Accept(self, visitor):
        visitor.GetManConclusion(self)


class Woman(Person):
    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)


class Action:
    def GetManConclusion(self, concreteElementA):
        pass

    def GetWomanConclusion(self, concreteElementB):
        pass


class Success(Action):
    def GetManConclusion(self, concreteElementA):
        print "xxxx"

    def GetWomanConclusion(self, concreteElementB):
        print "yyyy"


class Failure(Action):
    def GetManConclusion(self, concreteElementA):
        print "zzzz"

    def GetWomanConclusion(self, concreteElementB):
        print "qqqq"


class ObjectStructure:
    def __init__(self):
        self.plist = []

    def Add(self, p):
        self.plist = self.plist + [p]

    def Display(self, act):
        for p in self.plist:
            p.Accept(act)


if __name__ == "__main__":
    os = ObjectStructure()
    os.Add(Man())
    os.Add(Woman())
    sc = Success()
    os.Display(sc)
    fl = Failure()
    os.Display(fl)
