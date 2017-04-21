class BD(object):  # version 1
    def _query(self, query, type):
        print 'done'

    def execute(self, query):
        self._query(query, 'EXECUTE')

# BD.execute('my query')

instance = BD()
print instance.execute('my query')
