# -*- coding:utf-8 -*-
__author__ = 'raychang'


class IBread:
    def prepair(self):
        pass

    def kneadflour(self):
        pass

    def steamed(self):
        pass

    def process(self):
        pass


class AbstractBread(IBread):
    def __init__(self, bread):
        self.bread = bread

    def prepair(self):
        self.bread.prepair()

    def kneadflour(self):
        self.bread.kneadflour()

    def steamed(self):
        self.bread.steamed()

    def process(self):
        self.prepair()
        self.kneadflour()
        self.steamed()


class NormalBread(IBread):
    def prepair(self):
        print u'准备面粉, 水, 发酵粉!!'

    def kneadflour(self):
        print u'和面!!'

    def steamed(self):
        print u'蒸馒头!!'

    def process(self):
        self.prepair()
        self.kneadflour()
        self.steamed()


class CornDecorator(AbstractBread):
    def __init__(self, bread):
        AbstractBread.__init__(self, bread)

    def paint(self):
        print u'添加柠檬黄染色剂!!'

    def kneadflour(self):
        self.paint()
        AbstractBread.kneadflour(self)


class SweetDecorator(AbstractBread):
    def __init__(self, bread):
        AbstractBread.__init__(self, bread)

    def paint(self):
        print u'添加甜蜜素!!'

    def kneadflour(self):
        self.paint()
        AbstractBread.kneadflour(self)


if __name__ == '__main__':
    print u'====开始生产馒头===='
    normalbread = NormalBread()
    normalbread.process()
    print u'====生产馒头结束===='

    print u'====开始生产染色甜馒头===='
    normalbread = CornDecorator(normalbread)
    normalbread = SweetDecorator(normalbread)
    normalbread.process()
    print u'====生产染色甜馒头结束===='
