#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials("admin", "rabbit@1990")
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.60.101', '5672', '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "This is our second msg"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
    ))
print(" [x] Sent %r" % message)
connection.close()
