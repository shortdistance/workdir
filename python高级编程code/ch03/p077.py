def method(self):
    return 1

klass = type('MyClass', (object,), {'method': method})
instance = klass()
print instance.method()

class MyClass(object):
    def method(self):
        return 1

instance = MyClass()
print instance.method()
