def sum(*args):       # okay
    total = 0
    for arg in args:
        total += arg
    return total

def sum(sequence):    # better !
    total = 0
    for arg in sequence:
        total += arg
    return total

def make_sentence(**kw):
    noun = kw.get('noun', 'Bill')
    verb = kw.get('verb', 'is')
    adj = kw.get('adjective', 'happy')
    return '%s %s %s' % (noun, verb, adj)

def make_sentence(noun='Bill', verb='is', adjective='happy'):
    return '%s %s %s' % (noun, verb, adjective)
