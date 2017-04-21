# -*- coding:utf-8 -*-
__author__ = 'raychang'


class IUser:
    def receiveMessage(self, message):
        pass

    def sendMessage(self, message):
        pass

    def getMessage(self):
        pass


class IMediator:
    def regist(self, iuser):
        pass

    def notifyAllMessage(self, iuser):
        pass


class ConcreteMediator(IMediator):
    def __init__(self):
        self.user_list = []

    def regist(self, iuser):
        if iuser and iuser not in self.user_list:
            self.user_list.append(iuser)

    def notifyAllMessage(self, iuser):
        for x in self.user_list:
            if x and x != iuser:
                x.receiveMessage(iuser.getMessage())


class AbstractUser(IUser):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
        self.message = ''

    def sendMessage(self, message):
        self.message = message
        print u'%s说:%s' % (self.name, self.message)
        self.mediator.notifyAllMessage(self)

    def getMessage(self):
        return self.message


class UserA(AbstractUser):
    def __init__(self, mediator, name):
        AbstractUser.__init__(self, mediator, name)
        mediator.regist(self)

    def receiveMessage(self, message):
        print u'User A Received Message: %s' % message


class UserB(AbstractUser):
    def __init__(self, mediator, name):
        AbstractUser.__init__(self, mediator, name)
        mediator.regist(self)

    def receiveMessage(self, message):
        print u'User B Received Message: %s' % message


class UserC(AbstractUser):
    def __init__(self, mediator, name):
        AbstractUser.__init__(self, mediator, name)
        mediator.regist(self)

    def receiveMessage(self, message):
        print u'User C Received Message: %s' % message


if __name__ == '__main__':
    mediator = ConcreteMediator()
    usera = UserA(mediator, u'张三')
    userb = UserB(mediator, u'李四')
    userc = UserC(mediator, u'王五')

    print '================================'
    usera.sendMessage(u'大家好，我是张三')
    print '================================'
    print '================================'
    userb.sendMessage(u'我是李四，欢迎加入')
    print '================================'
    print '================================'
    userc.sendMessage(u'我是王五，欢迎加入')
    print '================================'
