# -*- coding:utf-8 -*-

def BinarySearch(l, key):
    low = 0
    high = len(l) - 1
    i = 0
    while (low <= high):
        i = i + 1
        mid = low + ((high - low) >> 1)
        if (l[mid] < key):
            low = mid + 1
        elif (l[mid] > key):
            high = mid - 1
        else:
            print"use %d times" % i
            return mid
    return -1

"""
def BinarySearch2(l, key):
    first = 0
    last = len(l) - 1

    if first <= last:
        midpoint = (first + last) // 2
        if key < l[midpoint]:
            print l[first:midpoint]
            templ  = l[first:midpoint]
            BinarySearch2(templ, key)
        elif key > l[midpoint]:
            print l[midpoint:last]
            templ  = l[midpoint:last]
            BinarySearch2(templ, key)
        else:
            return midpoint
    return -1
"""
def binSearch2(lst, item):
    mid = len(lst) //2
    index = -1
    if lst[mid] == item:
        index = mid
        return index
    if mid == 0:
        return index
    else:
        if item > lst[mid]:
            print lst[mid:]
            return binSearch2(lst[mid:], item)
        else:
            print lst[:mid]
            return binSearch2(lst[:mid], item)

if __name__ == "__main__":
    l = [1, 4, 5, 6, 7, 8, 9, 44, 333, 2233]
    print l
    print BinarySearch(l, 4)
    print binSearch2(l, 444)
    print BinarySearch(l, 44)
    print BinarySearch(l, 8)
    print BinarySearch(l, 2233)
    print BinarySearch(l, 77)
