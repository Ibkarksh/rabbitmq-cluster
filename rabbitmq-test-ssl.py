#!/usr/bin/env python
import logging
import pika
import ssl
from pika.credentials import ExternalCredentials

#logging.basicConfig(level=logging.INFO)
context = ssl.create_default_context(cafile="./roles/rabbitmq-conf-files/files/ssl/ca_certificate.pem")
context.load_cert_chain("./roles/rabbitmq-conf-files/files/ssl/client_nodeMQ01_certificate.pem",
                        "./roles/rabbitmq-conf-files/files/ssl/client_nodeMQ01_key.pem")

ssl_options = pika.SSLOptions(context, 'nodeMQ01')
conn_params = pika.ConnectionParameters(host='192.168.60.101',
                                        port=5671,
                                        ssl_options=ssl_options,
                                        credentials=ExternalCredentials())

with pika.BlockingConnection(conn_params) as conn:
    ch = conn.channel()
    ch.queue_declare("foobar-11")
    ch.basic_publish("", "foobar-11", "Hello, world!")
    print(ch.basic_get("foobar-11"))
    input("Press Enter to continue...")
