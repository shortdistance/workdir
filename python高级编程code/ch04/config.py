# config.py
SQL_USER = 'tarek'
SQL_PASSWORD = 'secret'
SQL_URI = 'postgres://%s:%s@localhost/db' % \
              (SQL_USER, SQL_PASSWORD)

MAX_THREADS = 4
