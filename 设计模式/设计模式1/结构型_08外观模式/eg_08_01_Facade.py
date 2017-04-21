#-*- coding:utf-8 -*-

__author__ = 'raychang'

#糖醋排骨接口
class ISpareribs:
    def prepair(self):
        pass

    def preserve(self):
        pass

    def fry(self):
        pass

    def juice(self):
        pass

#糖醋排骨实现
class Spareribs(ISpareribs):
    def prepair(self):
        print u'准备!'

    def preserve(self):
        print u'腌制!'

    def fry(self):
        print u'油炸!'

    def juice(self):
        print u'浇汁出锅!'

class ICookFacade:
    def cookSpareribs(self):
        pass

class CookFacade(ICookFacade):

    def __init__(self):
        self.spareribs = Spareribs()

    def cookSpareribs(self):
        self.spareribs.prepair()
        self.spareribs.preserve()
        self.spareribs.fry()
        self.spareribs.juice()

if __name__ == '__main__':
    print u'=======糖醋排骨制作开始======='
    cookfacade = CookFacade()
    cookfacade.cookSpareribs()
    print u'=======糖醋排骨制作结束======='
