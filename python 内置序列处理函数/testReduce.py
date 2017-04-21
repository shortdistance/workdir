#-*-coding:utf-8-*-
"""
reduce(function,seq[,init])
reduce()函数获得序列中前两个项，并把它传递给提供的函数，获得结果后再取序列中的下一项，连同结果再传递给函数，以此类推，直到处理完所有项为止。
"""
import operator
print reduce(operator.mul,[2,3,4,5]) # ((2*3)*4)*5

print reduce(operator.mul,[2,3,4,5],10) # (((1*2)*3)*4)*5

print reduce(operator.mul,[2,3,4,5],2) # (((2*2)*3)*4)*5

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print reduce(lambda x, y: x * y, foo)
