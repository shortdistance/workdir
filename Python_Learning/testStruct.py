#-*- coding:utf-8 -*-
import struct
from ctypes import create_string_buffer  

a = 'hello'
b = 'world1'
c = 2
d = 49.8

p = '%ds%dsif' %(len(a), len(b))

pSize = struct.calcsize(p)
buf = create_string_buffer(pSize)
ret = struct.pack_into(p, buf,  0, a, b, c, d)

print ret,  repr(buf.raw)

ret = struct.unpack_from(p, buf, 0)
print ret