#!/usr/bin/python
# page 270

from pbp.scripts.profiler import profile, stats
from collections import deque
my_list = range(100000)
my_deque = deque(range(100000))
@profile('by_list')
def by_list():
    my_list[500:502] = []

@profile('by_deque')
def by_deque():
    my_deque.rotate(500)
    my_deque.pop()
    my_deque.pop()
    my_deque.rotate(-500)

by_list();by_deque()
print stats['by_list']

print stats['by_deque']
 