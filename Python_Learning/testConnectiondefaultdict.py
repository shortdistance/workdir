#-*-coding:utf-8-*-
from collections import defaultdict
help(defaultdict)
#使用list初始化一个dict
d = defaultdict(list)
d["yellow"].append(1)
d["red"].append(2)
d["yellow"].append(3)
d['blue'] = 2
del(d['blue'])
d['blue'] = [4]
d['blue'].append(5)

print d


d1 = defaultdict(int)
d1['yellow']+=1
d1['blue']+=2
d1['yellow'] +=3
print d1