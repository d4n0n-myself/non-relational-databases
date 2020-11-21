import pika
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='my_test_load', exchange_type='topic')

routing_key = 'test.load'
message = 'Hello World!'

while True:
    channel.basic_publish(
        exchange='my_test_load', routing_key=routing_key, body=message)
    print(datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S:%f") + " [x] Sent %r:%r" % (routing_key, message))

connection.close()
