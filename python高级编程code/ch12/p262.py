#!/usr/bin/python
# page 262

from guppy import hpy

REPEAT = 100
def memory_grow(function, *args, **kw):
    """checks if a function makes the memory grows"""
    profiler = hpy()
    profiler.setref() 
    # 12 corresponds to the initial memory size
    # after a setref call
    start = profiler.heap().size + 12
    for i in range(REPEAT):
        function(*args, **kw)
    return profiler.heap().size - start

def stable():
    return "some"*10000

d = []
def greedy():
    for i in range(100):
        d.append('ouhuvugcgc'*i)

print memory_grow(stable)

print memory_grow(greedy)
