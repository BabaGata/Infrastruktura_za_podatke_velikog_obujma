import pika
import time
import random
from matplotlib import pyplot as plt

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

send_time = []

for no in range(100):
    message = f'Hello this is my message no{no}'
    
    start_time = time.time()
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    send_time.append(time.time() - start_time)

    print(f'sent message: {message}')
    # time.sleep(random.randint(1, 4))
    no += 1

channel.basic_publish(exchange='', routing_key='letterbox', body='stop')

plt.bar([i for i in range(100)], send_time)
plt.savefig(f'img/producer_{time.time()}.png')