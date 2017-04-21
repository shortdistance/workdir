# -*- coding: utf-8 -*-
import datetime
class GMT8(datetime.tzinfo):
    delta=datetime.timedelta(hours=8)
    def utcoffset(self,dt):
        return self.delta
    def tzname(self,dt):
        return "GMT+8"
    def dst(self,dt):
        return self.delta

class GMT(datetime.tzinfo):
    delta=datetime.timedelta(0)
    def utcoffset(self,dt):
        return self.delta
    def tzname(self,dt):
        return "GMT+0"
    def dst(self,dt):
        return self.delta 

from_tzinfo=GMT()  #格林威治时区，0时区
local_tzinfo=GMT8()#本地时区，+8区
gmt_time = datetime.datetime.strptime('2011-08-15 21:17:14', '%Y-%m-%d %H:%M:%S')
gmt_time = gmt_time.replace(tzinfo=from_tzinfo)
local_time = gmt_time.astimezone(local_tzinfo)

print from_tzinfo
print local_tzinfo

print from_tzinfo.dst(gmt_time)
print from_tzinfo.utcoffset(gmt_time)


print gmt_time
print local_time
