# -*-coding:utf-8-*-
'''
zip() in conjunction with the * operator can be used to unzip a list:
zip(x,y) 压缩, zip(*list) 带型号表示解压
'''

x = [1, 2, 3]
y = [4, 5, 6]
z = [5, 6, 7]
zipped = zip(x, y, z)
print zipped
x2, y2, z2 = zip(*zipped)

print x2, y2, z2
