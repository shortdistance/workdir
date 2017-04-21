# page 28 - 29
def power(values):
    for value in values:
        print 'powering %s' % value
        yield value

def adder(values):
    for value in values:
        print 'adding to %s' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

if __name__ == '__main__':
    elements = [1, 4, 7, 9, 12, 19]
    res = adder(power(elements))
    res.next()
    res.next()
    res.next()
