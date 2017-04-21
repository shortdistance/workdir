#!/usr/bin/python
# page 282

from processing import Process
import os
def work():
    print 'hey i am a process, id: %d' % os.getpid()

ps = []
for i in range(4):
    p = Process(target=work)
    ps.append(p)
    p.start()

print ps

for p in ps:
    p.join()

print ps
    