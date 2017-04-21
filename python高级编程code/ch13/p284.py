#!/usr/bin/python
# page 284

import random, timeit
from pbp.scripts.profiler import profile, print_stats
cache = {}
def square(n):
    return n * n

def cached_factory(n):
    if n in cache:
        cache[n] = square(n)
    return cache[n]

@profile('not cached')
def factory_calls():
    for i in xrange(100):
        square(random.randint(1, 10))

@profile('cached')
def cached_factory_calls():
    n = [random.randint(1, 10) for i in range(100)]
    #ns = [cached_factory(i) for i in n]

factory_calls(); 
cached_factory_calls();
print_stats()
