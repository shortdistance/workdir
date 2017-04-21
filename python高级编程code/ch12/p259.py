#!/usr/bin/python
# page 259
from guppy import hpy
profiler = hpy()

import random
def eat_memory():
    memory = []
    def _get_char():
        return chr(random.randint(97, 122))
    for i in range(100):
        size = random.randint(20, 150)
        data = [_get_char() for i in xrange(size)]
        memory.append(''.join(data))
    return '\n'.join(memory)

print profiler.iso(eat_memory())
print profiler.iso(eat_memory()+eat_memory())

g = hpy()
g.setrelheap()
print g.heap().size
print g.heap().size
print g.heap().size
