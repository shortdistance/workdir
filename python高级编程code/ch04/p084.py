OPTIONS = {}
def register_option(name):
    return OPTIONS.setdefault(name, 1 << len(OPTIONS))

def has_option(options, name):
    return bool(options & name)

# now defining options
BLUE = register_option('BLUE')
RED = register_option('RED')
WHITE = register_option('WHITE')

# let's try them
SET = BLUE | RED
print has_option(SET, BLUE)

print has_option(SET, WHITE)
