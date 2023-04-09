import socket
import json

s = socket.socket()

s.bind(("localhost", 5024))

s.listen(1)
print("Waiting for connections...")

mov = None
with open('horror.json','r') as f:
    mov = json.load(f)

while True:
    cli, addr = s.accept()
    print("Connected client:", addr)

    data = cli.recv(1024)

    result = json.dumps(mov)

    cli.send(result.encode('utf-8'))

    cli.close()
s.close()