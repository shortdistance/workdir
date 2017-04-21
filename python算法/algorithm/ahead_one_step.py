#!/usr/bin/env python
#coding:utf-8

"""
问题：

定义一个int型的一维数组，包含10个元素，分别赋值为1~10， 然后将数组中的元素都向前移一个位置，

即，a[0]=a[1],a[1]=a[2],…最后一个元素的值是原来第一个元素的值，然后输出这个数组。
"""

def ahead_one(lst):
    b = lst.pop(0)
    lst.append(b)
    return lst

if __name__ =="__main__":
    a = [i for i in range(1, 11)]
    print ahead_one(a)
    print ahead_one(a)
    print ahead_one(a)
    print ahead_one(a)
    print ahead_one(a)
