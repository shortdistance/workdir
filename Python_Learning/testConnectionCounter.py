#-*-coding:utf-8-*-
from collections import Counter

s1 = 'hello world,nihao,hi,zhangleid'
c1 = Counter(s1)
print c1
print c1.most_common(1)