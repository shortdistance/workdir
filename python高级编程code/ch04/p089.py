class Connection(object):
    _connected = []

    def connect(self, user):
        self._connected.append(user)

    @property
    def connected_people(self):
        return '\n'.join(self._connected)


my = Connection()
my.connect('Tarek')
my.connect('Shannon')
print my.connected_people
