#!/usr/bin/python
# page 280

import os
a = []
def some_work():
    a.append(2)
    child_pid = os.fork()
    if child_pid == 0:
        a.append(3)
        print "hey, i am the child process"
        print "my pid is %d" % os.getpid()
        print str(a)
    else:
        a.append(4)
        print "hey, i am the parent"
        print "the child is pid %d" % child_pid 
        print "I am the pid %d " % os.getpid()
        print str(a)

some_work()
