#-*-coding:utf-8-*-

#!/usr/bin/env python
#example8.py
#use UTF-8
#Python 3.3.0
#����: Event ��ʹ��
import threading
import time

event = threading.Event()

def func():
    # �ȴ��¼�������ȴ�����״̬
    print('%s wait for event...' % threading.currentThread().getName())
    event.wait()
    
    # �յ��¼����������״̬
    print('%s recv event.' % threading.currentThread().getName())

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()
 
time.sleep(2)
 
# �����¼�֪ͨ
print('MainThread set event.')
event.set()
