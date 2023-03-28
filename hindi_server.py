import socket

s = socket.socket()

s.bind(("localhost", 5023))


s.listen(1)
print("Waiting for connections...")

cli, addr = s.accept()
print("Connected client:", addr)

while True:
    data = cli.recv(1024).decode('utf-8')
    # msg = data.decode('utf-8')

    # if msg == 'Over':
    #     print("Connection over")
    #     break
    
    result = " "
    equation = data.split(" ")
    genre = equation[1]

    if genre == "Horror":
        PORT = 5028
    elif genre == "Detective":
        PORT = 5029
    elif genre == "Comedy":
        PORT = 5030
    elif genre == "Romance":
        PORT = 5031
   
    
    new_s = socket.socket()
    new_s.connect(("localhost", PORT))
    new_s.send(data.encode('utf-8'))
    result = new_s.recv(1024)
    new_s.close()

    cli.send(result)