#!/usr/bin/python
# page 290

MyType = type('MyType', (object,), {'a': 1})
ob = MyType()
print type(ob)

print ob.a

print isinstance(ob, object)
