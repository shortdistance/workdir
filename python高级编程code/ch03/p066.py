class UpperString(object):
    def __init__(self):
        self._value = ''
    def __get__(self, instance, klass):
        return self._value 
    def __set__(self, instance, value):
        self._value = value.upper()

class MyClass(object):
   attribute = UpperString()

instance_of = MyClass()
print instance_of.attribute

instance_of.attribute = 'my value'
print instance_of.attribute

instance_of.__dict__ = {}
instance_of.new_att = 1

print instance_of.__dict__

MyClass.new_att = UpperString()
print instance_of.__dict__

print instance_of.new_att 

instance_of.new_att = 'other value'
print instance_of.new_att 
print instance_of.__dict__

# page 67
class Whatever(object):
    def __get__(self, instance, klass):
        return 'whatever'

MyClass.whatever = Whatever()
print instance_of.__dict__

print instance_of.whatever
instance_of.whatever = 1
print instance_of.__dict__

