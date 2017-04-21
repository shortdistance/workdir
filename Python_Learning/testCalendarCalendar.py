#-*- coding:utf-8 -*-
import calendar

print calendar.setfirstweekday(calendar.MONDAY)
ca = calendar.Calendar()

print calendar.setfirstweekday(calendar.MONDAY)
print ca.firstweekday

for i in ca.iterweekdays():
    print i