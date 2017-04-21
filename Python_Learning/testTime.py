#! /usr/bin/python
# coding=utf-8

import time
from datetime import datetime

"""
表示日常所用时间的类，是用C实现的内嵌类。
功能比较简单，但效率高。表示的时间范围有限1970年1月1日到2038年1月19日。
"""

"""
当前时间
返回的一个float型，以一个固定时间epoch(1970年1月1日0时起经过的秒数)
因为time终究是以float型来表示的，所以对于timespan的问题，基本就成了数字问题。
"""
now = time.time()
print now
"""
使用localtime 返回一个time结构，
其中包括
tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst=0 夏令时间标志
tm_wday为周几，0是周一，6是周日
"""
now = time.localtime(time.time())
print now
# 如果是返回当前时间，可以简单的写成
print time.localtime()
# 这个返回UTC时间
print time.gmtime()

"""
转成字符串
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""
print time.strftime("%y%m%d%H%M%S", now)
# 如果打印当前时间，同样也可以简单的写成
strtime = time.strftime("%Y-%m-%d %H:%M:%S")

"""
字符串转成time结构
"""
time.strptime(strtime, "%Y-%m-%d %H:%M:%S")

"""
用tuple构建一个time结构
分别是年、月、日、小时、分、秒，后面两个都是0就好，自动计算出来。最后一个写成0
"""
past = (2010, 11, 12, 13, 14, 15, 0, 0, 0)
time.localtime(time.mktime(past))

"""
转成datetime型
http://www.cnblogs.com/goodspeed/archive/2011/11/06/python_datetime.html
"""
print datetime.fromtimestamp(time.time())
