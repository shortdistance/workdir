#!/usr/bin/python
# page 271

from collections import deque
from pbp.scripts.profiler import profile, stats
import sys
queue = deque()
def d_add_data(data):
    queue.appendleft(data)
 
def d_process_data():
    queue.pop()

BIG_N = 1000000
@profile('deque')
def sequence():
    for i in range(BIG_N):
        d_add_data(i)
    for i in range(BIG_N/2):
        d_process_data()
    for i in range(BIG_N):
        d_add_data(i)

lqueue = []
def l_add_data(data):
    lqueue.append(data)

def l_process_data():
    lqueue.pop(-1)

@profile('list')
def lsequence():
    for i in range(BIG_N):
        l_add_data(i)
    for i in range(BIG_N/2):
        l_process_data()
    for i in range(BIG_N):
        l_add_data(i)

sequence(); lsequence()
print stats['deque']

print stats['list']