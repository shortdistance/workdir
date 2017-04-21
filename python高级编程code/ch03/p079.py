def enhancer_1(klass):
    c = [l for l in klass.__name__ if l.isupper()] 
    klass.contracted_name = ''.join(c) 

def enhancer_2(klass):
    def logger(function):
        def wrap(*args, **kw):
            print 'I log everything !'
            return function(*args, **kw)
        return wrap
    for el in dir(klass):
        if el.startswith('_'):
            continue
        value = getattr(klass, el)
        if not hasattr(value, 'im_func'):
            continue
        setattr(klass, el, logger(value))

def enhance(klass, *enhancers):
    for enhancer in enhancers:
        enhancer(klass)

class MySimpleClass(object):
    def ok(self):
        """I return ok"""
        return 'I lied'

enhance(MySimpleClass, enhancer_1, enhancer_2)
thats = MySimpleClass()
print thats.ok()

#thats.score
print thats.contracted_name
