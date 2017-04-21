#-*-coding:utf-8-*-


import sets  
magic_chars = sets.Set('abracadabra')  
print magic_chars  
poping_chars = sets.Set('supercalifragilisticeexpialidocious')  
print poping_chars  
print "".join(magic_chars | poping_chars)  


l1 = ['zhang', 'lei', 'a', 'b', 'c','d','world','hello','a']
list_sets  = sets.Set(l1)
print list_sets

list_sets.add(123)
print list_sets
#list_sets.clear()
#print list_sets

l2 = ['zhang']
list_sets2 = sets.Set(l2)
print list_sets2

list_sets.difference_update(list_sets2)
print list_sets

list_sets.discard('a')
print list_sets

list_sets.pop()
print list_sets

try:
    list_sets.remove('a')
except Exception,e:
    print 'Error Info:', e


li3 = ['a', 'b', 'c']
li4 = ['b', 'c', 'd','e']
li_set1 = sets.Set(li3)
li_set2 = sets.Set(li4)
li_set1.update(li_set2)
print li_set1
print li_set2

'''

     |  add(self, element)
     |      Add an element to a set.
     |      
     |      This has no effect if the element is already present.
     |  
     |  clear(self)
     |      Remove all elements from this set.
     |  
     |  difference_update(self, other)
     |      Remove all elements of another set from this set.
     |  
     |  discard(self, element)
     |      Remove an element from a set if it is a member.
     |      
     |      If the element is not a member, do nothing.
     |  
     |  intersection_update(self, other)
     |      Update a set with the intersection of itself and another.
     |  
     |  pop(self)
     |      Remove and return an arbitrary set element.
     |  
     |  remove(self, element)
     |      Remove an element from a set; it must be a member.
     |      
     |      If the element is not a member, raise a KeyError.
     |  
     |  symmetric_difference_update(self, other)
     |      Update a set with the symmetric difference of itself and another.
     |  
     |  union_update(self, other)
     |      Update a set with the union of itself and another.
     |  
     |  update(self, iterable)
     |      Add all values from an iterable (such as a list or file).
'''