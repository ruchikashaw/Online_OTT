import socket

s = socket.socket()

s.bind(("localhost", 5027))


s.listen(1)
print("Waiting for connections...")

cli, addr = s.accept()
print("Connected client:", addr)

data = cli.recv(1024)



result = "Titanic"

cli.send(str(result).encode('utf-8'))


cli.close()