#!/usr/bin/python
# page 286

cache = {}
def get_key(function, *args, **kw):
    key = '%s.%s:' % (function.__module__,
                      function.__name__)
    hash_args = [str(arg) for arg in args]
    # of course, will work only if v is hashable
    hash_kw = ['%s:%s' % (k, hash(v)) 
               for k, v in kw.items()]
    return '%s::%s::%s' % (key, hash_args, hash_kw)     

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

@memoize()
def factory(n):
    return n * n

print factory(4)
print factory(4)
print factory(3)
print cache
