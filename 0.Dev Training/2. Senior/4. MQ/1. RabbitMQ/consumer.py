# -*-  coding:utf-8  -*-

__author__ = 'Adams'

import pika
import traceback

credentials = pika.PlainCredentials('admin', '123123')

connection = pika.BlockingConnection( pika.ConnectionParameters(
            '192.168.56.1', 5672, '/', credentials ) )

channel = connection.channel()

# You may ask why we celcare the queue again - wh have already ceclared it in out prvious code.
#
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

channel.queue_declare( queue = 'balance' )

def callback( ch, method, properties, body ):
    print(" [x] Received %r" % body )
    s = body.decode('utf-8')
    print(s)

channel.basic_consume( callback,
                       queue = 'balance',
                       no_ack= True )


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# 接收队列后, 查看一下队列状态
# [root@localhost ~]#  rabbitmqctl list_queues
# Listing queues ...
# balance    0
