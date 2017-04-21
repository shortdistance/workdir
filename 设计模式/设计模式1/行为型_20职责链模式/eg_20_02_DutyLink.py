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

class IHandler:
    def handleRequest(self, istudent):
        pass

    def setHandler(self, handler):
        pass

class AbstractHandler(IHandler):

    def __init__(self, state):
        self.state = state

    def process(self, istudent):
        pass

    def handleRequest(self, istudent):
        if istudent:
            if self.state ==istudent.getState():
                self.process(istudent)
            else:
                if self.handler:
                    print u'请求上级批示!!'
                    self.handler.handleRequest(istudent)

    def setHandler(self, handler):
        self.handler = handler

class SquardLeaderHandler(AbstractHandler):

    def __init__(self):
        AbstractHandler.__init__(self, 0)

    def process(self, istudent):
        print u'班长批复：', istudent.getRequestMessage()


class TeacherHandler(AbstractHandler):
    def __init__(self):
        AbstractHandler.__init__(self, 1)

    def process(self, istudent):
        print u'班主任批复：', istudent.getRequestMessage()

class SchoolMasterHandler(AbstractHandler):
    def __init__(self):
        AbstractHandler.__init__(self, 2)

    def process(self, istudent):
        print u'校长批复：', istudent.getRequestMessage()

class ProcessorHandler:
    processorhandler = None
    def __init__(self):
        self.squardleaderhandler = SquardLeaderHandler()
        self.teacherhandler = TeacherHandler()
        self.schoolmasterhandler = SchoolMasterHandler()
        self.squardleaderhandler.setHandler(self.teacherhandler)
        self.teacherhandler.setHandler(self.schoolmasterhandler)

    @classmethod
    def getInstance(cls):
        if cls.processorhandler:
            return cls.processorhandler
        else:
            cls.processorhandler = ProcessorHandler()
            return cls.processorhandler

    def sendMessage(self, istudent):
        self.squardleaderhandler.handleRequest(istudent)


if __name__ == '__main__':
    processorhandler = ProcessorHandler.getInstance()
    for i in range(0,3):
        rand = random.randint(0,2)
        student = Student(i, u'学生 %d 生病了, 要请假!!' % i )
        print '####################################'
        processorhandler.sendMessage(student)
        print '####################################'
