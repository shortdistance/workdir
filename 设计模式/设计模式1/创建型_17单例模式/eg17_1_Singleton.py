# -*- coding:utf-8 -*-
__author__ = 'raychang'


class Singleton:
    singleton = None

    def __init__(self):
        print '--this is Singleton!!!'

    @staticmethod
    def getInstance():
        if Singleton.singleton is None:
            Singleton.singleton = Singleton()
        return Singleton.singleton


if __name__ == '__main__':
    singleton = Singleton.getInstance()
    singleton1 = Singleton.getInstance()

    if singleton == singleton1:
        print 'This is the same object!!'
    else:
        print 'This is not the same object!!'
