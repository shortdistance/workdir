#!/usr/bin/python
# page 277

from Queue import Queue
import logging
import time 
import subprocess
q = Queue()
def index_file(filename):
    logging.info('indexing %s' % filename)
    f = open(filename)
    try:
        content = f.read()
        # external process is here
        subprocess.call(['converter.py'])
        time.sleep(0.5)
    finally:
        f.close()

def worker():
    while True:
        index_file(q.get())
        q.task_done()
