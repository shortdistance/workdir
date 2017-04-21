#-*-coding :utf-8-*-
import UserDict

ud1 = UserDict.UserDict()
ud1['1'] ='zhangleid' 
ud1[1]='hello'
ud1[2]='world'
print ud1.has_key('1')
print ud1.get('1')
print ud1.iteritems()
print ud1.iterkeys()
print ud1.itervalues()


print ud1.items()
print ud1.keys()
print ud1.values()
ud1.pop(1)
ud1.popitem()
print ud1
print ud1

ud2 = UserDict.UserDict()
ud2 = {'10':123, '11':234, 2:'hi'}
ud1.update(ud2)
print ud1
#ud1.clear()
#print ud1
