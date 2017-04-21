#-*- coding:utf-8 -*-
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

class CornBread(NormalBread):
    def paint(self):
        print u'添加柠檬黄染色剂!!'

    def kneadflour(self):
        self.paint()
        NormalBread.kneadflour(self)

class SweetBread(NormalBread):
    def paint(self):
        print u'添加甜蜜素!!'

    def kneadflour(self):
        self.paint()
        NormalBread.kneadflour(self)

if __name__ == '__main__':
    print u'====开始生产馒头===='
    normalbread = NormalBread()
    normalbread.process()
    print u'====生产馒头结束===='

    print u'====开始生产染色馒头===='
    cornbread = CornBread()
    cornbread.process()
    print u'====生产染色馒头结束===='

    print u'====开始生产甜馒头===='
    sweetbread = SweetBread()
    sweetbread.process()
    print u'====生产甜馒头结束===='