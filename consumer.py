import pika
import time

def on_message_recieved(ch, method, properties, body):
    if str(body).replace("b'", "").replace("'", "") == 'stop':
        print('Stopping consuming')
        ch.stop_consuming()
    
    print(f'recieved new message: {body}')
    time.sleep(0.1)
    ch.basic_ack(delivery_tag=method.delivery_tag)    

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox', on_message_callback=on_message_recieved)

print('starting consuming')

channel.start_consuming()
