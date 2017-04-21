# -*- coding:utf-8 -*-

__author__ = 'raychang'


class AbstractBaseFood:
    kind = ''
    num = 0
    price = 0.0

    def totalPrice(self):
        return self.num * self.price


class IFood:
    def printMessage(self):
        pass


class Hamburg(AbstractBaseFood, IFood):
    def printMessage(self):
        print u'--' + self.kind + u'风味汉堡,\t\t单价：%0.2f' % self.price + u',\t\t数量：%d' % self.num + u',\t\t合计：%0.2f' % self.totalPrice()


class ChickenWings(AbstractBaseFood, IFood):
    def printMessage(self):
        print u'--' + self.kind + u'风味鸡翅,\t\t单价：%0.2f' % self.price + u',\t\t数量：%d' % self.num + u',\t\t合计：%0.2f' % self.totalPrice()


class FrenchFries(AbstractBaseFood, IFood):
    def printMessage(self):
        print u'--' + self.kind + u'风味薯条,\t\t单价：%0.2f' % self.price + u',\t\t数量：%d' % self.num + u',\t\t合计：%0.2f' % self.totalPrice()


class Beverage(AbstractBaseFood, IFood):
    def printMessage(self):
        print u'--' + self.kind + u'饮料,\t\t单价：%0.2f' % self.price + u',\t\t数量：%d' % self.num + u',\t\t合计：%0.2f' % self.totalPrice()


class ChinaHamburg(Hamburg):
    def __init__(self, num=0):
        self.kind = u'麻辣'
        self.price = 14.0
        self.num = num


class ChinaChickenWings(ChickenWings):
    def __init__(self, num=0):
        self.kind = u'奥尔良'
        self.price = 2.5
        self.num = num


class ChinaFrenchFries(FrenchFries):
    def __init__(self, num=0):
        self.kind = u'普通'
        self.price = 8.0
        self.num = num


class ChinaBeverage(Beverage):
    def __init__(self, num=0):
        self.kind = u'可乐'
        self.price = 7.0
        self.num = num


class IKfcFactory(object):
    def createHamburg(self, num):
        pass

    def createChickenWings(self, num):
        pass

    def createFrenchFries(self, num):
        pass

    def createBeverage(self, num):
        pass


class ChinaKfcFactory(IKfcFactory):
    def createHamburg(self, num):
        return ChinaHamburg(num)

    def createChickenWings(self, num):
        return ChinaChickenWings(num)

    def createFrenchFries(self, num):
        return ChinaFrenchFries(num)

    def createBeverage(self, num):
        return ChinaBeverage(num)


class Customer(object):
    def __init__(self, kfc=None):
        self.kfc = kfc

    def orderHamburg(self, num):
        hamburg = self.kfc.createHamburg(num)
        hamburg.printMessage()
        return hamburg.totalPrice()

    def orderChickenWings(self, num):
        chickenwings = self.kfc.createChickenWings(num)
        chickenwings.printMessage()
        return chickenwings.totalPrice()

    def orderFrenchFries(self, num):
        frenchfries = self.kfc.createFrenchFries(num)
        frenchfries.printMessage()
        return frenchfries.totalPrice()

    def orderBeverage(self, num):
        beverage = self.kfc.createBeverage(num)
        beverage.printMessage()
        return beverage.totalPrice()


if __name__ == '__main__':
    kfc = ChinaKfcFactory()
    customer = Customer(kfc)

    hamburgMoney = customer.orderHamburg(1)
    chickenwingMoney = customer.orderChickenWings(4)
    frenchfriesMoney = customer.orderFrenchFries(1)
    beverageMoney = customer.orderBeverage(2)

    print u'总计：', hamburgMoney + chickenwingMoney + frenchfriesMoney + beverageMoney
