g = lambda x: x**2
print g(10)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [ (lambda x:x**2)(x) for x in l1]
print l2

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)
print make_incrementor(22)(33)



foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)