#!/usr/bin/python
# page 283

import processing
import Queue

print 'this machine has %d CPUs' \
        % processing.cpuCount()

def worker():
    file = q.get_nowait()
    return 'worked on ' + file
 
q = processing.Queue()
pool = processing.Pool()

for i in ('f1', 'f2', 'f3', 'f4', 'f5'):
    q.put(i)

while True:
    try:
        result = pool.apply_async(worker)
        print result.get(timeout=1)
    except Queue.Empty:
        break
