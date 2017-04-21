#-*- coding:utf-8 -*-

import repr

l1 = ['x'*1000, 'y'*100]
print repr.repr(l1)

rp = repr.Repr()

print 'maxlevel',rp.maxlevel
print 'maxdict',rp.maxdict
print 'maxlist',rp.maxlist
print 'maxtuple',rp.maxtuple
print 'maxset',rp.maxset
print 'maxfrozenset',rp.maxfrozenset
print 'maxdeque', rp.maxdeque
print 'maxarray', rp.maxarray
print 'maxlong', rp.maxlong
print 'maxstring',rp.maxstring

print 'maxother',rp.maxother

s1 = 'hello world'*100
print s1
s2 = rp.repr(s1)
print len(s2),s2

rp.maxstring=50
s3 = rp.repr(s1)
s4 = rp.repr1(s1,3)
print len(s3),s3
print len(s4),s4