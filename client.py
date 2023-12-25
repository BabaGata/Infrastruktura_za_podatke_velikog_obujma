import socket
import time

host = socket.gethostname()
port = 12345

client_socket = socket.socket()
client_socket.connect((host, port))

message = ''

while True:
    data = client_socket.recv(20).decode()
    if not data:
        break
    print(str(data))
    time.sleep(0.1)