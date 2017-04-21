import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
DATABASE_URL = 'postgres://ptfthxbyndigqo:bd6XgrHoSmM3KoHItWY01hk6QS@ec2-54-75-230-132.eu-west-1.compute.amazonaws.com:5432/d4pcuqjtknanio';
url = urlparse.urlparse(DATABASE_URL);

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cur = conn.cursor()
cur.execute(
'''SELECT "id", "name", "description", "failureMessage", "successMessage", "othersFailureMessage", "othersSuccessMessage", "type", "flags", "password", "createdAt", "updatedAt", "targetId", "locationId", "ownerId", "keyId" FROM "MUDObjects" AS "MUDObject" WHERE ((lower(name) LIKE '%tv%') AND ("MUDObject"."locationId" = 1 OR "MUDObject"."locationId" = 60 OR "MUDObject"."id" = 1));'''
)
rows = cur.fetchall()
for row in rows:
 print "ID = ", row[0]
 print "NAME = ", row[1]
conn.close()

