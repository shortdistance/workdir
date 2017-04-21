class weirdint(int):
    def __add__(self, other):
        return int.__add__(self, other) + 1
    def __repr__(self):
        return '<weirdo %d>' % self

    # public API
    def do_this(self):
        print 'this'
    def do_that(self):
        print 'that'

class BadHabits(object):
    def __my_method__(self):
        print 'ok'
