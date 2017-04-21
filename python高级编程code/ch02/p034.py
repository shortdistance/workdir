import itertools
def starting_at_five():
    value = raw_input().strip()
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = raw_input().strip()
 
iter = starting_at_five()
iter.next()
#one two three four five six

iter.next()
