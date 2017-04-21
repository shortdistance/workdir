#!/usr/bin/python
# -*- coding:utf-8 -*-
import base64
try:
    import hashlib
    hash = hashlib.md5()
except ImportError:
    # for Python << 2.5
    import md5
    hash = md5.new()
hash.update('1')
value = hash.digest()
print repr(value)   #得到的是二进制的字符串
print hash.hexdigest()  #得到的是一个十六进制的值
print base64.encodestring(value) #得到base64的值
