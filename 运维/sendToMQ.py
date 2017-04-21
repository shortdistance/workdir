#!/usr/bin/env python
#coding=utf8
import pika

mq = {
        'host': '172.16.9.144',
        'port': 5672,
        'user': 'svn',
        'pwd': '123456',
        'virt': 'svn',
        'exchange': 'securityte',
        'exchange_type': 'direct',
}

credentials = pika.PlainCredentials(mq['user'], mq['pwd'])
connection = pika.BlockingConnection(pika.ConnectionParameters(mq['host'], mq['port'], mq['virt'], credentials))

channel = connection.channel()
 
channel.queue_declare(queue='svn')
 
channel.basic_publish(exchange='securityte', routing_key='svn', body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()