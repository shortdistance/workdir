__author__ = 'Raychang'

#-*- coding:utf-8 -*-
import bisect

print dir(bisect)

l1 = [9, 33, 23, 44, 77, 66, 99, 88]
l1.sort()
print bisect.bisect_left(l1, 44)
print bisect.bisect_right(l1, 44)
print bisect.bisect(l1,44)

bisect.insort_left(l1, 44)
print l1
