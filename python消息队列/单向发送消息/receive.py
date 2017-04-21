#!/usr/bin/env python
#coding=utf8
import pika
 
mq = {
        'host': '172.16.9.144',
        'port': 5672,
        'user': 'rollen',
        'pwd': 'root',
        'virt': 'svn',
        'exchange': 'securityte',
        'exchange_type': 'direct',
}

credentials = pika.PlainCredentials(mq['user'], mq['pwd'])
connection = pika.BlockingConnection(pika.ConnectionParameters(mq['host'], mq['port'], credentials))

channel = connection.channel()
 
channel.queue_declare(queue='svn')
 
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
 
channel.basic_consume(callback, queue='svn', no_ack=True)
 
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
