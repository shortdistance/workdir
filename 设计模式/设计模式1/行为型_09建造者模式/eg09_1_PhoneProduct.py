# -*- coding:utf-8 -*-
__author__ = 'raychang'


class MobilePackage(object):
    def __init__(self):
        money = 0.0
        shortinfo = 0
        music = ''

    def getMoney(self):
        return self.money

    def setMoney(self, money):
        self.money = money

    def getShortInfo(self):
        return self.shortinfo

    def setShortInfo(self, shortinfo):
        self.shortinfo = shortinfo

    def getMusic(self):
        return self.music

    def setMusic(self, music):
        self.music = music


class IMobileBuilder:
    def buildMoney(self):
        pass

    def buildShortInfo(self):
        pass

    def buildMusic(self):
        pass

    def getMobilePackage(self):
        pass


class AbstractBasePackage:
    def __init__(self):
        self.mobilepackage = MobilePackage()


class MobileBuildImpl1(IMobileBuilder, AbstractBasePackage):
    def buildMoney(self):
        self.mobilepackage.setMoney(20.0)

    def buildShortInfo(self):
        self.mobilepackage.setShortInfo(400)

    def buildMusic(self):
        self.mobilepackage.setMusic(u'天使')

    def getMobilePackage(self):
        return self.mobilepackage


class MobileBuildImpl2(IMobileBuilder, AbstractBasePackage):
    def buildMoney(self):
        self.mobilepackage.setMoney(30.0)

    def buildShortInfo(self):
        self.mobilepackage.setShortInfo(600)

    def buildMusic(self):
        self.mobilepackage.setMusic(u'大海')

    def getMobilePackage(self):
        return self.mobilepackage


class MobileDirector:
    def createMobilePackage(self, mobilebuilder):
        if mobilebuilder:
            mobilebuilder.buildMoney()
            mobilebuilder.buildShortInfo()
            mobilebuilder.buildMusic()
            return mobilebuilder.getMobilePackage()
        else:
            return None


def printMessage(mobilepackage):
    print u'--话费:',mobilepackage.getMoney(),u'\t短信:',mobilepackage.getShortInfo(),u'条\t彩铃:',mobilepackage.getMusic()


if __name__ == '__main__':
    mobiledirector = MobileDirector()
    mobilebuildimpl1 = MobileBuildImpl1()
    mobilebuildimpl2 = MobileBuildImpl2()
    mp1 = mobiledirector.createMobilePackage(mobilebuildimpl1)
    mp2 = mobiledirector.createMobilePackage(mobilebuildimpl2)
    printMessage(mp1)
    printMessage(mp2)