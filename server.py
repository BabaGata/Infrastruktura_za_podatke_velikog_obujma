import socket
import time
import random
from matplotlib import pyplot as plt

host = socket.gethostname()
port = 12345

server_socket = socket.socket()

server_socket.bind((host, port))

server_socket.listen(1)
conn, address = server_socket.accept()
print("Connection from: " + str(address))

send_time = []

for no in range(100):
    message = f'This is message no{no}'

    start_time = time.time()    
    conn.send(message.encode())
    send_time.append(time.time() - start_time)

    print(f'Sending message no{no}')
    # time.sleep(random.randint(1, 4))
    no += 1

conn.close()

plt.bar([i for i in range(100)], send_time)
plt.savefig(f'img/server_{time.time()}.png')