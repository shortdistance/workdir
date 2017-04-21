#!/usr/bin/python
# page 294

from StringIO import StringIO
my_file = StringIO(u'some content')
print my_file.read()

my_file.seek(0)
print my_file.read(1)
