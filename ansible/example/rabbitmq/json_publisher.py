# json_publisher.py
import pika, os, logging, json
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='caitprocess') # Declare a queue
# send a message

msg = {'cait': 'tool', 'version': '0.1', 'value': 34.567, 'resx': 1920, 'resy': 1080}

#channel.basic_publish(exchange='', routing_key='caitprocess', body='Cait Json Message')
channel.basic_publish(exchange='', routing_key='caitprocess', body=json.dumps(msg))
print ("[x] Message sent to consumer")
connection.close()

