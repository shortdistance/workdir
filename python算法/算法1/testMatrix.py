# -*- coding:utf-8 -*-
__author__ = 'Raychang'

a, b, c, d, e, f, g, h = range(8)

#     a b c d e f g h
print '--------matrix1--------'
N = [[0, 1, 1, 1, 1, 1, 0, 0],  # a 如果要加上weight值，把1换成weight即可
     [0, 0, 1, 0, 1, 0, 0, 0],  # b
     [0, 0, 0, 1, 0, 0, 0, 0],  # c
     [0, 0, 0, 0, 1, 0, 0, 0],  # d
     [0, 0, 0, 0, 0, 1, 0, 0],  # e
     [0, 0, 1, 0, 0, 0, 1, 1],  # f
     [0, 0, 0, 0, 0, 1, 0, 1],  # g
     [0, 0, 0, 0, 0, 1, 1, 0]]  # h

print N[a][b]
print sum(N[f])


print '--------matrix2--------'
# 更好的方法是把infinite weight用float('inf')表示
_ = float('inf')
W = [[0, 2, 1, 3, 9, 4, _, _],
     [_, 0, 4, _, 3, _, _, _],
     [_, _, 0, 8, _, _, _, _],
     [_, _, _, 0, 7, _, _, _],
     [_, _, _, _, 0, 5, _, _],
     [_, _, 2, _, _, 0, 2, 2],
     [_, _, _, _, _, 1, 0, 6],
     [_, _, _, _, _, 9, 8, 0]]

print W[a][b]
print W[c][e]
print sum(1 for w in W[a])

print '--------matrix3--------'
N = [[0]*10 for i in range(10)]
# in NumPy, you can use the  zeros  function:
import numpy as np
N = np.zeros([10,10])
print N