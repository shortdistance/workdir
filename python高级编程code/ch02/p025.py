# first: old method
i = 0
seq = ["one", "two", "three"]
for element in seq:
    seq[i] = '%d: %s' % (i, seq[i])
    i += 1
print seq

# second: more python
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
    seq[i] = '%d: %s' % (i, seq[i])
print seq

# third: best python
def _treatment(pos, element):
    return '%d: %s' % (pos, element)
 
seq = ["one", "two", "three"]
print [_treatment(i, el) for i, el in enumerate(seq)]
