#coding=utf8
import datetime
from datetime import timedelta

from datetime import datetime,timedelta   
now = datetime.now()   
yesterday = now - timedelta(days=1)   
tomorrow = now + timedelta(days=1)   
next_year = now + timedelta(days = 365)  

print now
print yesterday
print tomorrow
print next_year

print timedelta(days=1)   
print timedelta(days = 365)  

print timedelta.resolution


from datetime import datetime,time,date

print datetime.today()
print datetime.now()
print datetime.utcnow()

d = datetime.date(2014, 3, 12)
t = datetime.time(1,12,23,200)
print datetime.combine(d, t)