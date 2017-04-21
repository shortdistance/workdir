#-*-coding:utf-8-*-
#!/usr/bin/env python   
#example6.py   
#use UTF-8   
#Python 3.3.0   

import threading  
import time  
   
#��Ʒ 
product = None  
#��������   
con = threading.Condition()  
   
#�����߷���   
def produce(): 
    if con.acquire():  
        while True:  
            if product is None:  
                print 'produce...'
                product = 'anything'  
                  
                # ֪ͨ�����ߣ���Ʒ�Ѿ�����   
                con.notify() 

            # �ȴ�֪ͨ   
            con.wait()  
            time.sleep(2)  
   
# �����߷���   
def consume():  
    if con.acquire():  
        while True:  
            if product is not None:  
                print 'consume...' 
                product = None  
                # ֪ͨ�����ߣ���Ʒ�Ѿ�û��   
                con.notify()  
              
            # �ȴ�֪ͨ   
            con.wait()  
            time.sleep(2) 
            
global product     
t1 = threading.Thread(target=produce)  
t2 = threading.Thread(target=consume)  
t2.start()  
t1.start()  
