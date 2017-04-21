#-*-coding:utf-8-*-

import Queue
myqueue = Queue.Queue(maxsize = 2)

myqueue.put(1)
myqueue.put(2)
print myqueue.empty()
print myqueue.full()
s = myqueue.get()
s1 = myqueue.get()
if myqueue.qsize()>0:
    s2=myqueue.get()


print myqueue
print s
print s1
print myqueue.qsize()
print myqueue.task_done()