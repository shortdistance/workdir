#-*- coding:utf-8 -*-

import base64
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()
strB64 = '''
Tk5O
L25wYWdlL2N1c3RtbmcvczM3NzAvZjM3NzBfbWFpbi5odG1s
MjIwMTYwMjAwMDI0NDY4Njg4
MTU4MDQ0MjU5MDQ=
MTExNTA3MjUwMDAwMDAwMDAwMDE4NjY3OA==
'''
print base64.decodestring(strB64)

