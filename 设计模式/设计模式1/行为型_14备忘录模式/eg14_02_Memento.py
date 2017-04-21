# -*-coding:utf-8 -*-
import random

__author__ = 'raychang'

class INarrowMemento:
    pass

class Memento(INarrowMemento):
    def __init__(self, blood, sword):
        self.blood = blood
        self.sword = sword

    def getBlood(self):
        return self.blood

    def getSword(self):
        return self.sword


class Hero:
    def __init__(self):
        self.blood = 100
        self.sword = 100

    def createMemento(self):
        print u'创建备忘录...'
        return Memento(self.blood, self.sword)

    def restoreFromMemento(self, memento):
        print u'恢复备忘录中的状态...'
        if memento:
            memento1 = memento
            self.blood = memento1.getBlood()
            self.sword = memento1.getSword()

    def toString(self):
        return u'当前血液值:%s - 当前武力值:%s' % (self.blood, self.sword)

    def koBoss(self):
        if self.blood <= 0 or self.sword <= 0:
            print self.toString()
            print u'挑战Boss失败...'
            return -1
        else:
            win = random.random()
            if win < 0.02:
                print self.toString()
                print u'恭喜你,挑战Boss成功...'
                return 1
            else:
                print self.toString()
                print u'继续挑战...'
                bloodint = random.randint(1, 10)
                swordint = random.randint(1, 10)
                self.blood -= bloodint
                self.sword -= swordint
                return 0


class Caretaker:
    def __init__(self):
        self.memento = None

    def getMemento(self):
        return self.memento

    def setMemento(self, memento):
        self.memento = memento


if __name__ == '__main__':
    hero = Hero()
    caretaker = Caretaker()
    caretaker.setMemento(hero.createMemento())
    cnt = 1
    ko = -1
    while ko != 1 and cnt <= 3:
        print u'第%d次挑战...' % cnt
        ko = hero.koBoss()

        while True:
            if ko == -1:
                hero.restoreFromMemento(caretaker.getMemento())
                cnt += 1
                break
            elif ko == 0:
                ko = hero.koBoss()

            elif ko == 1:
                break
