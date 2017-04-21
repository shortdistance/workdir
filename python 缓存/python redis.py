__author__ = 'Raychang'

import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
"""
for i in xrange(0, 100000):
    redisClient.hset(i, "id", i)
    redisClient.hset(i, "name", 'test%d' % i)
    redisClient.hset(i, "password", 'passwd%d' % i)
    redisClient.hset(i, "email", 'email%d' % i)
    redisClient.hset(i, "phone", 'phone%d' % i)
"""

for i in xrange(0, 100000):
    id = redisClient.hget(i, "id")
    name =  redisClient.hget(i, "name")
    password =  redisClient.hget(i, "password")
    email =  redisClient.hget(i, "email")
    phone =  redisClient.hget(i, "phone")
    print id
    #print id, name, password, email, phone
    