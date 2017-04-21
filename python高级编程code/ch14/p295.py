#!/usr/bin/python
# page 295

from os.path import split, splitext
class DublinCoreAdapter(object):
    def __init__(self, filename):
        self._filename = filename
    def title(self):
        return splitext(split(self._filename)[-1])[0]
    def creator(self):
        return 'Unknown'         # we could get it for real
    def languages(self):
        return ('en',)

class DublinCoreInfo(object):
    def summary(self, dc_ob):
        print 'Title: %s' % dc_ob.title()
        print 'Creator: %s' % dc_ob.creator()
        print 'Languages: %s' % \
                  ', '.join(dc_ob.languages())

adapted = DublinCoreAdapter('example.txt')
infos = DublinCoreInfo()
print infos.summary(adapted)
