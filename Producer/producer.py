import pika
import time

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

starttime = []
endtime = []

for no in range(1000):    
    starttime.append(time.time())
    channel.basic_publish(exchange='', routing_key='letterbox', body='Hello world!')
    endtime.append(time.time())

    print(f'sent message no.{no}')

with open('producer_out.data', 'w') as file:
    file.write("starttime\tttime\tendtime\n")
    for i in range(len(starttime)):
        file.write(f"{starttime[i]}\t{endtime[i]-starttime[i]}\t{endtime[i]}\n")

channel.basic_publish(exchange='', routing_key='letterbox', body='stop')

connection.close()