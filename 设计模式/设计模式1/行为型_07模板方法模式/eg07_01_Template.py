# -*- coding:utf-8 -*-
__author__ = 'raychang'


class AbstractPeople:
    def getUp(self):
        print u'起床...'

    def haveBreakfast(self):
        pass

    def transport(self):
        pass

    def doWork(self):
        print u'工作...'

    def dayLife(self):
        print '==============================='
        self.getUp()
        self.haveBreakfast()
        self.transport()
        self.doWork()
        print '==============================='


class PeopleA(AbstractPeople):
    def haveBreakfast(self):
        print u'A吃早餐，牛奶和三明治!!'

    def transport(self):
        print u'A开私家车上班!!'


class PeopleB(AbstractPeople):
    def haveBreakfast(self):
        print u'B吃包子，豆浆!!'

    def transport(self):
        print u'B坐公交车上班!!'


class PeopleC(AbstractPeople):
    def haveBreakfast(self):
        print u'C吃饼，鸡蛋!!'

    def transport(self):
        print u'C做地铁上班!!'


if __name__ == '__main__':
    peoplea = PeopleA()
    peopleb = PeopleB()
    peoplec = PeopleC()

    peoplea.dayLife()
    peopleb.dayLife()
    peoplec.dayLife()
