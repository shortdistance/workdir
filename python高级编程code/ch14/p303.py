#!/usr/bin/python
# page 303

import os

def visit(directory, visitor):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # foo.txt -> .txt
            ext = os.path.splitext(file)[-1][1:]
            if hasattr(visitor, ext):
                getattr(visitor, ext)(file)

class FileReader(object):
    def pdf(self, file):
        print 'processing %s' % file

walker = visit('/home/11', FileReader())
