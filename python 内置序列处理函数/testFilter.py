# -*-coding:utf-8-*-
"""序列处理函数
常用函数中的len()、max()和min()同样可用于序列。

filter(function,list)
调用filter()时，它会把一个函数应用于序列中的每个项，并返回该函数返回真值时的所有项，从而过滤掉返回假值的所有项。
"""

s = ["bad", "good", "bade", "we"]
print filter(lambda s: s.find("bad") == -1, s)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)


nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)
    print nums
print nums
