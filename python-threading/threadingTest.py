# encoding: UTF-8
import threading
import time

"""
class MyThread(threading.Thread):
    def do1(self):
        global resA, resB
        if mutexA.acquire():
            msg = self.name + ' got resA'
            print msg

            if mutexB.acquire(1):
                msg = self.name + ' got resB'
                print msg
                mutexB.release()
            mutexA.release()

    def do2(self):
        global resA, resB
        if mutexB.acquire():
            msg = self.name + ' got resB'
            print msg

            if mutexA.acquire(1):
                msg = self.name + ' got resA'
                print msg
                mutexA.release()
            mutexB.release()

    def run(self):
        self.do1()
        self.do2()


resA = 0
resB = 0

mutexA = threading.Lock()
mutexB = threading.Lock()


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
"""

"""
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.release()
num = 0
mutex = threading.RLock()
def test():
    for i in range(100):
        t = MyThread()
        t.start()

test()
"""

"""
import threading
import time

mutex1 = threading.RLock()
def worker(i):
    if mutex1.acquire(1):
        print(i)
        time.sleep(1)
        print("AWAKE")
        mutex1.release()


for i in xrange(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
print("closed")
"""


import threading
import time
import Queue

class Producer(threading.Thread):
    def run(self):
        #global count
        global myqueue
        while True:
            if con.acquire():
                if myqueue.full():
                    con.wait()
                else:
                    if myqueue.empty():
                        max_num = 1
                    else:
                        max_num = myqueue.queue[-1] + 1
                    myqueue.put(max_num)
                    msg = self.name+' produce 1, num=' + str(max_num)
                    print msg
                    con.notify()
                con.release()
                #time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        #global count
        global myqueue
        while True:
            if con.acquire():
                if myqueue.empty():
                    con.wait()
                else:
                    num = myqueue.get()
                    msg = self.name+' consume 1, num='+str(num)
                    print msg
                    con.notify()
                con.release()
                time.sleep(0.5)


myqueue = Queue.Queue(maxsize = 500)
con = threading.Condition()

def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()