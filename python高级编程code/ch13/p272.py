#!/usr/bin/python
# page 272

from collections import defaultdict
from pbp.scripts.profiler import profile, stats
s = [('yellow', 1), ('blue', 2), ('yellow', 3), 
     ('blue', 4), ('red', 1)]
@profile('defaultdict')
def faster():
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
  
@profile('dict')
def slower():
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)

slower(); faster()
print stats['dict']

print stats['defaultdict']
