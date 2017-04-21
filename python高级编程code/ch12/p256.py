#!/usr/bin/python
# page 256
import time
import sys
if sys.platform == 'win32':    # same condition in timeit
    timer = time.clock
else:
    timer = time.time
from test import pystone

benchtime, pystones = pystone.pystones()
def seconds_to_kpystones(seconds):
    if seconds == 0:
        return 0
    return (pystones*seconds) / 1000 

stats = {}

def duration(name='stats', stats=stats):
    def _duration(function):
        def __duration(*args, **kw):
            start_time = timer()             
            try:
                return function(*args, **kw)
            finally:
                total = timer() - start_time
                kstones = seconds_to_kpystones(total)
                stats[name] = total, kstones 
        return __duration
    return _duration

@duration()
def some_code():
    time.sleep(0.5)

some_code()
print stats
