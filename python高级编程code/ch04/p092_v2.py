import logging

class BD(object): # version 2
    def _query(self, query, type, logger):
        logger('done')
    def execute(self, query, logger=logging.info):
        self._query(query, 'EXECUTE', logger)

#BD.execute('my query') # old stype call

instance = BD()
print instance.execute('my query', logging.warning)
