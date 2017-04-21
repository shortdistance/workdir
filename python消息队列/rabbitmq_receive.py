#-*-coding:utf-8-*-
#!/usr/bin/env python
#rabbitmq.py

import pika
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mq = {
        'host': '172.16.9.144',
        'port': 5672,
        'user': 'svn',
        'pwd': '123456',
        'virt': 'svn',
        'exchange': 'securityte',
        'exchange_type': 'direct',
}

class MQRouting():
        """rabbitmq操作类,广播消息到所有队列，各队列进行消息筛选"""
        def __init__(self):
                credentials = pika.PlainCredentials(mq['user'], mq['pwd'])
                self.conn = pika.BlockingConnection(pika.ConnectionParameters(mq['host'], mq['port'], mq['virt'], credentials))
                self.channel = self.conn.channel()
                self.channel.exchange_declare(exchange=mq['exchange'], type=mq['exchange_type'])
                logger.info('Rabbitmq连接已建立，host={}, port={}'.format(mq['host'], mq['port']))

        def public(self, routing_key, msg):
                """发布消息"""
                self.channel.basic_publish(
                        exchange = mq['exchange'],
                        routing_key = routing_key,
                        body=msg,
                        properties=pika.BasicProperties(
                                delivery_mode = 2, # make message persistent
                        )
                )
                logger.info('消息已发布：{}:{}'.format(routing_key,msg))

        def consume(self, routing_key):
                """接收消息"""
                def callback(ch, method, properties, body):
                        print " [x] Received %r" % (body,)
                self.channel.queue_declare(queue=routing_key)
                self.channel.queue_bind(exchange=mq['exchange'], queue=routing_key, routing_key=routing_key)
                self.channel.basic_consume(callback, queue=routing_key, no_ack=True)
                self.channel.start_consuming()

        def close(self):
                if self.channel: self.channel.close()
                if self.conn: self.conn.close()


if __name__ == '__main__':
        routing = MQRouting()
        routing.consume('first')
        