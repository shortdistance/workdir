#-*- coding:utf-8 -*-

import string

s1 = 'zhangleid hello world!'
print string.ascii_letters 
print string.ascii_lowercase 
print string.ascii_uppercase 
print string.digits 
print string.hexdigits 
print string.letters 
print string.lowercase 
print string.octdigits 
print string.punctuation 
print string.printable 
print string.uppercase 
print string.whitespace


s='a123'
print s.capitalize()
print string.capitalize(s)

print s.center(8, '-')
print string.center(s, 8, '-')

s='a12b123cd12e12345'
print s.count('12')
print s.count('45',4)
print s.count('45', 0)
print s.count('45', 0, -1)


import string
help(string)



s = 'zhangleid'
s.capitalize()
string.capitalize(s)
s.center(100, 'c')
