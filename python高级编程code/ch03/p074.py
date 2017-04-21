class Frozen(object):
    __slots__ = ['ice', 'cream']

print '__dict__' in dir(Frozen)

print 'ice' in dir(Frozen)

glagla = Frozen()
glagla.ice = 1
glagla.cream = 1
print glagla
print glagla.ice
print glagla.cream

#glagla.icy = 1
