#!/usr/bin/python
# page 297

class Url(object):
    def __init__(self, location):
        self._url = urlopen(location)
    def headers(self):
        return dict(self._url.headers.items())
    def get(self):
        return self._url.read()

python_org = Url('http://python.org')
print python_org.headers()
