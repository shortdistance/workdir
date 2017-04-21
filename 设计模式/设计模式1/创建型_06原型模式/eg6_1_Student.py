# -*-coding:utf-8 -*-
__author__ = 'raychang'
import copy


class DayLife:
    def __init__(self):
        self.getUp = ''
        self.byBus = ''
        self.getFood = ''
        self.noon = ''
        self.afternoonWork = ''
        self.goHome = ''
        self.night = ''

    def setGetUp(self, getUp):
        self.getUp = getUp

    def setByBus(self, byBus):
        self.byBus = byBus

    def setGetFood(self, getFood):
        self.getFood = getFood

    def setNoon(self, noon):
        self.noon = noon

    def setAfternoonWork(self, afternoonWork):
        self.afternoonWork = afternoonWork

    def setGoHome(self, goHome):
        self.goHome = goHome

    def setNight(self, night):
        self.night = night

    def printDayLife(self):
        print self.getUp
        print self.byBus
        print self.getFood
        print self.noon
        print self.afternoonWork
        print self.goHome
        print self.night

    def clone(self):
        return copy.deepcopy(self)


class ILifeFactory:
    def getNewInstance(self):
        pass


class LifeFactoryImpl(ILifeFactory):
    def __init__(self):
        self.daylife = None

    def getNewInstance(self):
        print u'New Daylife!!'
        if self.daylife:
            self.daylife = self.daylife.clone()
        else:
            self.daylife = DayLife()
            self.daylife.setGetUp(u'7:00起床!!')
            self.daylife.setByBus(u'7:30公交车!!')
            self.daylife.setGetFood(u'8:30到公司附近公交站下车!!')
            self.daylife.setNoon(u'12:00午餐在公司附近解决，午餐后在工位休息一下!!')
            self.daylife.setAfternoonWork(u'1:30开始工作!!')
            self.daylife.setGoHome(u'5:30准时下班!!')
            self.daylife.setNight(u'晚上休闲娱乐!!')
        return self.daylife


if __name__ == '__main__':
    lifefactory = LifeFactoryImpl()
    daylife = lifefactory.getNewInstance()
    daylife.printDayLife()
    print '==============================='

    daylife_new = lifefactory.getNewInstance()
    daylife_new.setGetUp(u'7:30才起床啊!!')
    daylife_new.printDayLife()

    print '==============================='
    daylife_new1 = lifefactory.getNewInstance()
    daylife_new1.printDayLife()
