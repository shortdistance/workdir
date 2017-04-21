#!/usr/bin/python
# page 288

import time
from datetime import datetime
cache = {}

def get_key(function, *args, **kw):
    key = '%s.%s:' % (function.__module__,
                      function.__name__)
    hash_args = [str(arg) for arg in args]
    # of course, will work only if v is hashable
    hash_kw = ['%s:%s' % (k, hash(v)) 
               for k, v in kw.items()]
    return '%s::%s::%s' % (key, hash_args, hash_kw)     

def memoize(get_key=get_key, storage=cache, age=0):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = get_key(function, *args, **kw)
            try:
                value_age, value = storage[key]
                deprecated = (age != 0 and 
                             (value_age+age) < time.time())                              
            except KeyError:
                deprecated = True 
            
            if not deprecated:
                return value
            storage[key] = time.time(), function(*args, **kw)             
            return storage[key][1]
        return __memoize
    return _memoize 

from datetime import datetime
@memoize(age=30)
def what_time():
    return datetime.now().strftime('%H:%M')

what_time()

print cache
