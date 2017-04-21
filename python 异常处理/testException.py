# -*- coding:utf-8 -*-
__author__ = 'Raychang'

import time
import sys

class myException(Exception):
    pass


def test_KeyboardInterrupt():
    i = 0
    while 1:
        try:
            i = i + 1
            print i
            time.sleep(2)
        except KeyboardInterrupt, e:
            print u'退出程序！'
            break


def test_ZeroDivisionError():
    try:
        a = 10
        b = 0
        print a / b
    except ZeroDivisionError, e:
        print u'除零错误，已经处理！'
        pass


def test_exc_info():
    try:
        a = b
        b = c
    except:
        info = sys.exc_info()
        print info[0], ":", info[1]


def test_raise_exception():
    raise myException


if __name__ == "__main__":
    #test_KeyboardInterrupt()
    # test_raise_exception()
    # test_ZeroDivisionError()
    test_exc_info()