#-*- coding:utf-8 -*-
import random

__author__ = 'raychang'

class IStudent:
    def getState(self):
        pass

    def getRequestMessage(self):
        pass


class Student(IStudent):
    def __init__(self, state, message):
        self.state = state
        self.message = message

    def getState(self):
        return self.state

    def getRequestMessage(self):
        return self.message

class IHandle:
    def handleRequest(self):
        pass

class AbstractHandle(IHandle):
    def process(self, istudent):
        pass

    def handleRequest(self, istudent):
        if istudent:
            self.process(istudent)


class SquardLeaderHandle(AbstractHandle):
    def process(self, istudent):
        print u'班长批复：', istudent.getRequestMessage()


class TeacherHandle(AbstractHandle):
    def process(self, istudent):
        print u'班主任批复：', istudent.getRequestMessage()

class SchoolMasterHandle(AbstractHandle):
    def process(self, istudent):
        print u'校长批复：', istudent.getRequestMessage()

class ProcessorHandle:
    processorhandle = None
    def __init__(self):
        self.squardleaderhandle = SquardLeaderHandle()
        self.teacherhandle = TeacherHandle()
        self.schoolmasterhandle = SchoolMasterHandle()

    @classmethod
    def getInstance(cls):
        if cls.processorhandle:
            return cls.processorhandle
        else:
            cls.processorhandle = ProcessorHandle()
            return cls.processorhandle

    def sendMessage(self, istudent):
        if istudent.getState() == 0:
            self.squardleaderhandle.handleRequest(istudent)
        else:
            print u'请求上级批示!!'
            if istudent.getState() == 1:
                self.teacherhandle.handleRequest(istudent)
            else:
                print u'请求上级批示!!'
                if istudent.getState() == 2:
                    self.schoolmasterhandle.handleRequest(istudent)


if __name__ == '__main__':
    processorhandle = ProcessorHandle.getInstance()
    for i in range(0,3):
        rand = random.randint(0,2)
        student = Student(i, u'学生 %d 生病了, 要请假!!' % i )
        print '####################################'
        processorhandle.sendMessage(student)
        print '####################################'
