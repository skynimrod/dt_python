# -*-  coding:utf-8  -*-

import pika
import traceback

try:
    credentials = pika.PlainCredentials('admin','123123')
    connection = pika.BlockingConnection( pika.ConnectionParameters(
        '192.168.56.1', 5672, '/', credentials ))
    channel = connection.channel()

    # 声明 Queue, durable为True时,队列持久化; exclusive为True时,建立临时队列
    channel.queue_declare( queue = 'balance', durable=True, exclusive=False )

    # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.

    channel.basic_publish(  exchange = '',
                            routing_key = 'balance',
                            body = 'url|比上年同期增长：' )
    print(" [x] Send 'Hello World!' ")
    connection.close()
except:
    traceback.print_exc()
