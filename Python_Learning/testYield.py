# -*- coding:utf-8 -*-
def fib(max):
    a, b = 1, 1
    while a < max:
        # print a
        yield a
        a, b = b, a + b


f = fib(1000)
n = f.next()
print n
while n:
    n = f.next()
    print n
