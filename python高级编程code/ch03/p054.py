class DistinctError(Exception):
    pass

class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            # keys() and values() will return
            # corresponding lists 
            # as long as the dict is not changed
            # between the two calls
            # otherwise the dict type does not guarantee
            # the ordering.
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError(("This value already exists for '%s'") % \
                                       str(self[existing_key]))
        except ValueError:
            pass
        super(distinctdict, self).__setitem__(key, value)

my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value1'

#my['other_key'] = 'value2'
print my
