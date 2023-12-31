import pika
import time

starttime = []
endtime = []

def on_message_recieved(ch, method, properties, body):
    if str(body).replace("b'", "").replace("'", "") == 'stop':
        print('Stopping consuming')
        ch.basic_ack(delivery_tag=method.delivery_tag)
        ch.stop_consuming()
    else:
        print(f'recieved new message: {body}')
        starttime.append(time.time())
        time.sleep(10)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        endtime.append(time.time())

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox', on_message_callback=on_message_recieved)

print('starting consuming')

channel.start_consuming()

with open('consumer_out.data', 'a') as file:
    for i in range(len(starttime)):
        file.write(f"{starttime[i]}\t{endtime[i]-starttime[i]}\t{endtime[i]}\n")