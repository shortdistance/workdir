# -*- coding:utf-8 -*-
__author__ = 'Raychang'

# filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：
# 函数的返回是bool型的;
def f(x):
    return x % 2 != 0 and x % 3 != 0


print filter(f, range(2, 25))
print filter(lambda x:x % 2 != 0 and x % 3 != 0, range(2,25))

s1 = 'hello world'
def s(x):
    return x not in ['h', 'e']

print filter(s, s1)
print filter(lambda x:x not in ['h', 'e'], s1)

# map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：
def cube(x):
    return x * x * x


print map(cube, [x for x in range(1, 11) if x % 2 == 0])
print map(lambda x: x*x*x, [x for x in range(1, 11) if x % 2 == 0])

def add(x, y):
    return x + y

print reduce(add, range(1, 11))
print reduce(lambda x,y:x+y, range(1, 11))

def mutiply(x, y):
    return x * y

print reduce(mutiply, range(1, 11))
print reduce(lambda x,y:x*y, range(1, 11))

g = lambda x, y: x + y
print g(20, 30)
