#!/usr/bin/env python
#example1.py
#use UTF-8
#Python 3.3.0
import threading 
def func():
    print('func() passed to Thread')
	
t = threading.Thread(target=func)
t.start()