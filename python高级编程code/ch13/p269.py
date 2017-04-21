#!/usr/bin/python
# page 269

seq = ['a', 'a', 'b', 'c', 'c', 'd']
res = []
for el in seq:
    if el not in res:
        res.append(el)

print res
