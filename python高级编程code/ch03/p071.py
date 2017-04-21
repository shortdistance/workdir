class MyClass(object):
    def __init__(self):
        self._my_secret_thing = 1
    def _i_get(self):
        return self._my_secret_thing

    def _i_set(self, value):
        self._my_secret_thing = value

    def _i_delete(self):
        print 'neh!'

    my_thing = property(_i_get, _i_set, _i_delete, 'the thing')

instance_of = MyClass()
print instance_of.my_thing

instance_of.my_thing = 3
print instance_of.my_thing

del instance_of.my_thing

help(instance_of)
