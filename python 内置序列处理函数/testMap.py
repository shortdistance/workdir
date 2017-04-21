# -*-coding:utf-8-*-
"""
map(function,list[,list])
map()函数把一个函数应用于序列中所有项，并返回一个列表。
"""
import string

l1 = ["python", "zope", "linux"]
print map(lambda s: s.capitalize(), l1)

"""
map()还可同时应用于多个列表。如：
"""
import operator

s = [1.0, 2, 3];
t = [3.0, 2, 1]
print map(lambda x, y: x / y, s, t)
print map(lambda x, y: x + y, s, t)

"""
如果传递一个None值，而不是一个函数，则map()会把每个序列中的相应元素合并起来，并返回
该元组。如：
"""
a = [1, 2];
b = [3, 4];
c = [5, 6]
d = [10,11]

print map(None, a, b, c, d)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print map(lambda x: x * 2 + 10, foo)
