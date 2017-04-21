#URL:http://blog.sina.com.cn/s/blog_6b60259a0101diss.html
#-*-coding:utf-8 -*-
__author__ = 'Raychang'
s1 = range(1,10)
print len(s1)
for i in range(len(s1)) :
    print s1[i]

N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

print N['a']