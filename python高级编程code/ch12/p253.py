#!/usr/bin/python
# page 253

import time
import sys
if sys.platform == 'win32':    # same condition in timeit
    timer = time.clock
else:
    timer = time.time
stats = {}
def duration(name='stats', stats=stats):
    def _duration(function):
        def __duration(*args, **kw):
            start_time = timer()             
            try:
                return function(*args, **kw)
            finally:
                stats[name] = timer() - start_time 
        return __duration
    return _duration

from myapp import heavy
heavy = duration('this_func_is')(heavy)
heavy()
print stats['this_func_is']

stats = {}
from myapp import light
import myapp
myapp.light = duration('myapp.light')(myapp.light)
myapp.main()
print stats
