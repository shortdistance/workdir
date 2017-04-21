#!/usr/bin/python
# page 268

def find(seq, el):
    pos = bisect(seq, el)
    if pos==0 or (pos==len(seq) and seq[-1]!=el):
        return -1
    return pos - 1

seq = [2, 3, 7, 8, 9]
find(seq, 9)
