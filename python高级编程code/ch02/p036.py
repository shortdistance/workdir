from itertools import groupby
def compress(data):
    return ((len(list(group)), name) for name, group in groupby(data))

def decompress(data):
    return (car * size for size, car in data)

l1 = 'get uuuuuuuuuuuuuuuuuup'
compressed = compress('get uuuuuuuuuuuuuuuuuup')
print list(compressed)

d = ''.join(decompress(compress('get uuuuuuuuuuuuuuuuuup')))
print d