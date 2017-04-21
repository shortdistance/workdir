class folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self):
        print 'I am the %s folder.' % self.name
        for element in self:
            print element


the = folder('secret')
print the

the.append('pics')
the.append('videos')
the.dir()
