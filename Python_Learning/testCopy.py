#-*-coding:utf-8-*-

import copy

a=[1,2,3,4,['a','b','c']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)

print id(a)
print id(b)
print id(c)
print id(d)

a[4].append('d')

print a[4],id(a[4])
print b[4],id(b[4])
print c[4],id(c[4])
print d[4],id(d[4])