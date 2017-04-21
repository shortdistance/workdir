#-*- coding:utf-8 -*-

__author__ = 'raychang'

class IRedWine:
    def product(self):
        pass

    def sell(self):
        pass

class RealRedWineFactory(IRedWine):
    def product(self):
        print u'红酒酒厂生产红酒!!'

    def sell(self):
        print u'红酒酒厂销售红酒!!'

class RedWineProxy(IRedWine):
    def __init__(self, redwine):
        self.permission = True
        self.redWine = redwine

    def product(self):
        if self.permission:
            print u'这是合法的红酒代理商!!'
            print u'代理商接到订单，通知红酒酒厂生产!!'
            self.redWine.product()
        else:
            print u'这是非法的红酒代理商!!'

    def sell(self):
        if self.permission:
            print u'这是合法的红酒代理商!!'
            self.redWine.sell()
            print u'红酒代理商从酒厂拿到红酒, 高价卖出, 赚取一定的差价!!'

        else:
            print u'这是非法的红酒代理商!!'

if __name__ == '__main__':
    realredwinefactory = RealRedWineFactory()
    redwineproxy = RedWineProxy(realredwinefactory)
    redwineproxy.product()
    redwineproxy.sell()