#-*-coding:utf-8-*-

import array
a = array.array("B", range(96,120,1)) # unsigned char
a1 = array.array("B", range(32,40,1))
b = array.array("L", range(16)) # signed short
print 'a~~~~',a
print 'a.tostring()~~~~',repr(a.tostring())
print 'b~~~~',b
print 'repr(b.tostring())~~~~',repr(b.tostring())

print a.buffer_info()

a.append(121) 

print a.buffer_info()

a.byteswap()
print a

a.extend(a1)
print a

print a.count(32)

l1 = [211,222,233,244]
a2 = array.array("B")
a2.fromlist(l1)
print a2


a3 = array.array("hello world,how are you")
print a3
#-- append a new item to the end of the array
#buffer_info() -- return information giving the current memory info
#byteswap() -- byteswap all the items of the array
#count() -- return number of occurrences of an object
#extend() -- extend array by appending multiple elements from an iterable
#fromfile() -- read items from a file object
#fromlist() -- append items from the list
#fromstring() -- append items from the string
#index() -- return index of first occurrence of an object
#insert() -- insert a new item into the array at a provided position
#pop() -- remove and return item (default last)
#read() -- DEPRECATED, use fromfile()
#remove() -- remove first occurrence of an object
#reverse() -- reverse the order of the items in the array
#tofile() -- write all items to a file object
#tolist() -- return the array converted to an ordinary list
#tostring() -- return the array converted to a string
#write() -- DEPRECATED, use tofile()
