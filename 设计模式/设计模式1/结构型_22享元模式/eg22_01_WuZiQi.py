# -*- coding:utf-8 -*-
import random
__author__ = 'raychang'


class AbstractChessman:
    def __init__(self, chess):
        self.chess = chess

    def show(self):
        print self.chess,'(',self.x,',',self.y,')'

    def point(self, x, y):
        pass

class BlackChessman(AbstractChessman):
    def __init__(self):
        AbstractChessman.__init__(self, "*")
        print '---Blackchessman Construction Exec!!!---'

    def point(self, x, y):
        self.x = x
        self.y = y
        self.show()


class WhiteChessman(AbstractChessman):
    def __init__(self):
        AbstractChessman.__init__(self, "0")
        print '---Whitechessman Construction Exec!!!---'

    def point(self, x, y):
        self.x = x
        self.y = y
        self.show()


class FiveChessmanFactory:
    cache = {}
    fiveChessmanFactory = None

    @classmethod
    def getInstance(cls):
        if cls.fiveChessmanFactory:
            return cls.fiveChessmanFactory
        else:
            cls.fiveChessmanFactory = FiveChessmanFactory()
            return cls.fiveChessmanFactory

    def getChessmanObject(cls, c):
        abstractchessman = cls.cache.get(c)
        if abstractchessman is None:
            if c == 'B':
                abstractchessman = BlackChessman()
            elif c == 'W':
                abstractchessman = WhiteChessman()
            else:
                pass

            if abstractchessman:
                cls.cache[c] = abstractchessman
        return abstractchessman


if __name__ == '__main__':
    fivechessmanfactory = FiveChessmanFactory.getInstance()
    rand = 0
    abstractchessman = None

    for i in range(0,10):
        rand = random.randint(0,1)
        if rand == 0:
            abstractchessman = fivechessmanfactory.getChessmanObject('B')
        elif rand == 1:
            abstractchessman = fivechessmanfactory.getChessmanObject('W')

        if abstractchessman:
            abstractchessman.point(i, random.randrange(0,15))
