#-*- coding:utf-8 -*-
__author__ = 'raychang'


class AbsBasePower:
    def __init__(self, power):
        self.power = power
        self.unit = 'V'

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit


class IPower220:
    def output220V(self):
        pass


class Power220(AbsBasePower, IPower220):
    def __init__(self):
        AbsBasePower.__init__(self, 220)

    def output220V(self):
        print u'----这是[%s%s]电源!----' % (self.getPower(), self.getUnit())


class IPower12:
    def output12V(self):
        pass


class Power12(AbsBasePower, IPower12):
    def __init__(self):
        AbsBasePower.__init__(self, 12)

    def output12V(self):
        print u'----这是[%s%s]电源!----' % (self.getPower(), self.getUnit())


class AdapterPower12(IPower12):
    def __init__(self, absBasePower):
        self.absBasePower = absBasePower

    def output12V(self):
        powerfloat = self.absBasePower.getPower()

        if powerfloat == 380:
            powerfloat = powerfloat / 31.67

        elif powerfloat == 220:
            powerfloat = powerfloat / 18.33

        elif powerfloat == 110:
            powerfloat = powerfloat / 9.17

        else:
            print u'----不能适配电源!----'
            return

        powerfloat = int(powerfloat)
        print u'----这是[%s%s]电源!----' % (powerfloat, self.absBasePower.getUnit())


if __name__ == '__main__':
    power220 = Power220()
    power12 = Power12()

    power220.output220V()
    power12.output12V()

    print u'----电源适配器转换中!----'
    adapterpower12 = AdapterPower12(power220)
    adapterpower12.output12V()
    print u'----电源适配器转换结束!----'