class Mama(object):     # this is the old way
    def says(self):
        print 'do your homework'

class Sister(Mama):
    def says(self): 
        Mama.says(self)
        print 'and clean your bedroom'

anita = Sister()
anita.says()
