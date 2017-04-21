#!/usr/bin/python
# page 273

from collections import namedtuple 
Customer = namedtuple('Customer', 'firstname lastname')

c = Customer(u'Tarek', u'carl shen')
print c.firstname
