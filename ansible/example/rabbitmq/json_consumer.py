# json_consumer.py
import pika, os, time, json

def cait_process_function(msg):
  print(" ContentAI Tool (CAIT) processing")
  print(" Received %r" % msg)

  cait = json.loads(msg)

  print(" CAIT : ", cait['cait']);
  print(" VERSION : ", cait['version']);
  print(" x : ", cait['resx'], " y : ", cait['resy']);
  print(" value : ", cait['value']);


  time.sleep(5) # delays for 5 seconds
  print(" CAIT processing finished");
  return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='caitprocess') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  cait_process_function(body)

# set up subscription on the queue
channel.basic_consume(callback,
  queue='caitprocess',
  no_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()

