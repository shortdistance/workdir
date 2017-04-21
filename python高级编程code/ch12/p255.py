#!/usr/bin/python
# page 255
from test import pystone

print pystone.pystones()

benchtime, pystones = pystone.pystones()
def seconds_to_kpystones(seconds):
    if seconds == 0:
        return 0
    return (pystones*seconds) / 1000 

print seconds_to_kpystones(0.03)
print seconds_to_kpystones(1)
print seconds_to_kpystones(2)

