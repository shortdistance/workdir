# -*-coding:utf-8 -*-
__author__ = 'raychang'


class AbstractSword:
    name = ""

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name


class QiXingSword(AbstractSword):
    name = u'七星宝刀'


class BaXingSword(AbstractSword):
    name = u'八星宝刀'


class ISwordFactory:
    def createSword(self):
        pass


class QiXingFactory(ISwordFactory):
    def createSword(self):
        return QiXingSword()


class BaXingFactory(ISwordFactory):
    def createSword(self):
        return BaXingSword()


if __name__ == '__main__':
    qxF = QiXingFactory()
    qx = qxF.createSword()
    print qx.getName()

    bxF = BaXingFactory()
    bx = bxF.createSword()
    print bx.name
