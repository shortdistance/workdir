# -*- coding:utf-8 -*-

__author__ = 'raychang'


class ILight:
    def electricConnected(self):
        pass

    def light(self):
        pass

    def electricClosed(self):
        pass


class BaseSwitch:
    def __init__(self, light):
        self.light = light

    def makeLight(self):
        self.light.electricConnected()
        self.light.light()
        self.light.electricClosed()


class RemoteControlSwitch(BaseSwitch):
    def __init__(self, light):
        BaseSwitch.__init__(self, light)

    def makeRemoteLight(self, operColor):
        self.light.electricConnected()
        self.light.light()

        color = ''
        if operColor == 1:
            color = u'暖色'

        elif operColor == 2:
            color = u'蓝色'

        elif operColor == 3:
            color = u'红色'

        else:
            color = u'白色'

        print u'...现在是：%s' % color

        self.light.electricClosed()


class IncandescentLight(ILight):
    def electricConnected(self):
        print u'白炽灯打开了!!'

    def light(self):
        print u'白炽灯照明!!'

    def electricClosed(self):
        print u'白炽灯关闭了!!'


class CrystalLight(ILight):
    def electricConnected(self):
        print u'水晶灯打开了!!'

    def light(self):
        print u'水晶灯照明!!'

    def electricClosed(self):
        print u'水晶灯关闭了!!'


if __name__ == '__main__':
    incandescentlight = IncandescentLight()
    crystallight = CrystalLight()

    print u'---一般开关!---'
    switch1 = BaseSwitch(incandescentlight)
    switch1.makeLight()

    print u'---远程开关!---'
    switch2 = RemoteControlSwitch(crystallight)
    switch2.makeRemoteLight(1)
