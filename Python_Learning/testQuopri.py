#-*- encoding: gbk-*-
import quopri

a = "only a test数据"
b = quopri.encodestring(a) # 对字符串编码
print b
print quopri.decodestring(b) # 对字符串解码

