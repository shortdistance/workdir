#-*- encoding: gbk-*-
import quopri

a = "only a test����"
b = quopri.encodestring(a) # ���ַ�������
print b
print quopri.decodestring(b) # ���ַ�������

