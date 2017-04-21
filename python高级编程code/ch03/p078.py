# copy from page 68
class API(object):
    def _print_values(self, obj):
        def _print_value(key):
            if key.startswith('_'):
                return ''
            value = getattr(obj, key)
            if not hasattr(value, 'im_func'):
                doc = type(value).__name__
            else:
                if value.__doc__ is None:
                    doc = 'no docstring'
                else:
                    doc = value.__doc__
            return '             %s : %s' % (key, doc)
        res = [_print_value(el) for el in dir(obj)]
        return '\n'.join([el for el in res if el != ''])

    def __get__(self, instance, klass):
        if instance is not None:
            return self._print_values(instance)
        else:
            return self._print_values(klass)

# page 78, but need API in page 68
def equip(classname, base_types, dict):
    if '__doc__' not in dict:
        dict['__doc__'] = API()
    return type(classname, base_types, dict)

class MyClass(object):
    __metaclass__ = equip
    def alright(self):
        """the ok method"""
        return 'okay'

ma = MyClass()
print ma.__class__

print ma.__class__.__dict__['__doc__']   # __doc__ is replaced !

ma.y = 6
print ma.__doc__
