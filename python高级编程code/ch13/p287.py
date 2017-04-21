#!/usr/bin/python
# page 287

import random, timeit
from pbp.scripts.profiler import profile, print_stats
cache = {}
import md5 
def get_key(function_called, n):
    return md5.md5(str(n)).hexdigest()

def memoize(get_key=get_key, cache=cache):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = get_key(function, *args, **kw)
            try:
                return cache[key] 
            except KeyError:
                cache[key] = function(*args, **kw) 
                return cache[key]
        return __memoize
    return _memoize

def square(n):
    return n * n

@memoize(get_key)
def cached_factory(n):
    return n * n
 
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
