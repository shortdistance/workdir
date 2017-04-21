class Mama(object):     # this is the new way
    def says(self):
        print 'do your homework'

class Sister(Mama):
    def says(self): 
        super(Sister, self).says()
        print 'and clean your bedroom'

anita = Sister()
anita.says()
