# -*- coding:utf-8 -*-
__author__ = 'raychang'
import random


class IObserver:
    def update(self, subject):
        pass


class ISubject:
    def add(self, observer):
        pass

    def remove(self, observer):
        pass

    def notifyAllObserver(self):
        pass

    def setTemperature(self, temperature):
        pass

    def temperatureReport(self):
        pass


class Subject(ISubject):
    def __init__(self):
        self.observer_list = []
        self.warningLevel = ''
        self.temperature = 0

    def add(self, observer):
        if observer and observer not in self.observer_list:
            self.observer_list.append(observer)
            return True
        else:
            return False

    def remove(self, observer):
        self.observer_list.remove(observer)

    def notifyAllObserver(self):
        print u'==========气象部门发布高温%s警报!==========' % self.warningLevel
        for x in self.observer_list:
            x.update(self)

    def invoke(self):
        if 35 <= self.temperature < 37:
            self.warningLevel = u'黄色'
        elif 37 <= self.temperature < 40:
            self.warningLevel = u'橙色'
        elif self.temperature >= 40:
            self.warningLevel = u'红色'
        self.notifyAllObserver()

    def setTemperature(self, temperature):
        self.temperature = temperature
        self.invoke()

    def temperatureReport(self):
        return u'温度:%s' % self.temperature


class PersonObserver(IObserver):
    def update(self, subject):
        print u'个人收到高温预警：%s' % subject.temperatureReport()


class GovernmentObserver(IObserver):
    def update(self, subject):
        print u'政府收到高温预警：%s' % subject.temperatureReport()


class CompanyObserver(IObserver):
    def update(self, subject):
        print u'企业收到高温预警：%s' % subject.temperatureReport()


if __name__ == '__main__':
    subject = Subject()
    subject.add(PersonObserver())
    subject.add(GovernmentObserver())
    subject.add(CompanyObserver())
    for i in range(0,10):
        subject.setTemperature(random.randint(35, 42))
