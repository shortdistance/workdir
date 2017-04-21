#-*- coding:utf-8 -*-

#!/usr/bin/env python   
   
from threading import Thread   
import subprocess   
from Queue import Queue   
   
num_threads=3   
ips=['127.0.0.1','180.97.33.107']   
q=Queue()   
def pingme(i,queue):   
    while True:   
        ip=queue.get()   
        print 'Thread %s pinging %s' %(i,ip)   
        ret=subprocess.call('ping -n 100 %s' % ip,shell=True,stdout=open('c:\\1.txt','w'),stderr=subprocess.STDOUT)   
        #这里就是我们所需要的stdout的编码格式 
        if ret==0:   
            print '%s is alive!' %ip   
        elif ret==1:   
            print '%s is down...'%ip   
        queue.task_done()   
   
#start num_threads threads   
for i in range(num_threads):   
    t=Thread(target=pingme,args=(i,q))   
    t.setDaemon(True)   
    t.start()   
   
for ip in ips:   
    q.put(ip)   
print 'main thread waiting...'   
q.join();print 'Done'   
