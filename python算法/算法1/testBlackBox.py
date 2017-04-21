#-*- coding:utf-8 -*-
__author__ = 'Raychang'

from random import randrange
L = [randrange(10000) for i in range(1000)]
print L
print 42 in L #liner

S = set(L)
print S
print 9 in S #constant
