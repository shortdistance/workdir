__author__ = 'Raychang'

from random import randrange


def MinDistance(seq):
    dd = float("inf")
    xx = yy = 0
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d
    return xx, yy, dd


seq = [randrange(2 ** 8) for i in range(10)]
xx, yy, dd = MinDistance(seq)
print xx, yy, dd


def MinDistanceBySort(seq):
    seq.sort()
    dd = float("inf")
    xx = yy = 0
    for i in range(len(seq) - 1):
        x, y = seq[i], seq[i + 1]
        if x == y: continue
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy, dd

seq = [randrange(2 ** 8) for i in range(10)]
print seq
xx, yy, dd = MinDistanceBySort(seq)
print xx, yy, dd