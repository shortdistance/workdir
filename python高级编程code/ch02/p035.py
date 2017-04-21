import itertools
def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable,2)
    return list(itertools.islice(a, headsize)), b


seq = range(1,100)

print with_head(seq)
print with_head(seq, 4)
