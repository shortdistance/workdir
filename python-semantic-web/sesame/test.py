url = 'http://localhost:8080'
path = '/openrdf-sesame/'
user = 'admin'
password = 'admin'
repository = 'my_openrdf'

# ----------------------------

from pysesame.pySesame import SesameConnection
connection = SesameConnection('http://localhost:8080', '/openrdf-sesame/')
print connection
#connection.login('admin', 'admin')
#connection.repositories()