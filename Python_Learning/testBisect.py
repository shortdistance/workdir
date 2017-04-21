#-*-coding:utf-8-*-

import bisect
l1 = [30, 50, 30]
l1.sort()
bisect.insort(l1, 25)
bisect.insort(l1, 15)
bisect.insort(l1, 500)
print l1

l2 = ['zhanglei', 'abc', 'hello world']
l2.sort()
bisect.insort(l2,'abd')
bisect.insort(l2,'jump')
print l2

import math
i = 0
if i:
    print i


print bisect.bisect(l2, 'hello world')
print bisect.bisect_left(l2, 'hello world')
print bisect.bisect_right(l2, 'hello world')

if i:
    try:
        pass
    finally:
        pass

print l2
bisect.insort(l2, 'zzz')
print l2
bisect.insort_right(l2, 'zzz1')
print l2
bisect.insort_left(l2, 'zzz2')
print l2
