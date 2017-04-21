# coding:utf-8

"""
python的Thread类中还提供了join()方法，使得一个线程可以等待另一个线程执行结束后再继续运行。
这个方法还可以设定一个timeout参数，避免无休止的等待。因为两个线程顺序完成，看起来象一个线程，所以称为线程的合并。一个例子：
"""
import threading
import random
import time


class MyThread(threading.Thread):
    def run(self):
        wait_time = random.randrange(1, 10)
        print "%s will wait %d seconds" % (self.name, wait_time)
        time.sleep(wait_time)
        print "%s finished!" % self.name


if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = MyThread()
        t.start()
        threads.append(t)
    print 'main thread is waitting for exit...'
    for t in threads:
        t.join(1)

    print 'main thread finished!'
