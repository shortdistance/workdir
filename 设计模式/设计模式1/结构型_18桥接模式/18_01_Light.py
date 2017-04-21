# -*- coding:utf-8 -*-

__author__ = 'raychang'


class AbstractSwitch:
    def turnOn(self):
        pass

    def light(self):
        pass

    def turnOff(self):
        pass

    def makeLight(self):
        self.turnOn()
        self.light()
        self.turnOff()


class IncandescentLight(AbstractSwitch):
    def turnOn(self):
        print u'白炽灯打开了!!'

    def light(self):
        print u'白炽灯照明!!'

    def turnOff(self):
        print u'白炽灯关闭了!!'


class CrystalLight(AbstractSwitch):
    def turnOn(self):
        print u'水晶灯打开了!!'

    def light(self):
        print u'水晶灯照明!!'

    def turnOff(self):
        print u'水晶灯关闭了!!'

    def makeRemoteLight(self, operColor):
        self.turnOn()
        self.light()

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

        self.turnOff()

if __name__ == '__main__':
    incandescentlight = IncandescentLight()
    crystallight = CrystalLight()

    incandescentlight.makeLight()
    crystallight.makeRemoteLight(1)