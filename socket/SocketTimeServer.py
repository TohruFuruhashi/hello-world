import socket
import datetime

PORT = 55555

while True:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("", PORT))

    server.listen()

    client, addr = server.accept()

    now = datetime.datetime.now()

    client.send(str(now).encode())

    print(str(now))

    client.close()

    server.close()
