class MeanElephant(object):
    def __init__(self):
        self._people_to_kill = []
    def is_slapped_on_the_butt_by(self, name):
        self._people_to_kill.append(name)
        print 'Ouch!'
    def revenge(self):
        print '10 years later...'
        for person in self._people_to_kill:
            print 'Me kill %s' % person 

joe = MeanElephant()
joe.is_slapped_on_the_butt_by('Tarek')
joe.is_slapped_on_the_butt_by('Bill')
joe.revenge()
