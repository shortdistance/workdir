from contextlib import contextmanager

@contextmanager
def context():
    print 'entering the zone'
    try:
        yield
    except Exception, e:
        print 'with an error (%s)' % e
        raise e
    else:
        print 'with no error'

with context():
    print 'i am the zone'

with context():
    print 'i am the buggy zone'
    raise TypeError('i am the bug')
