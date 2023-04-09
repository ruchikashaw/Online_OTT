import socket

s = socket.socket()

s.bind(("localhost", 5021))


s.listen(1)
print("Waiting for connections...")

while True:
    cli, addr = s.accept()
    print("Connected client:", addr)
    data = cli.recv(1024).decode('utf-8')
    # msg = data.decode('utf-8')

    # if msg == 'Over':
    #     print("Connection over")
    #     break
    
    result = " "
    equation = data.split(" ")
    print(equation)
    genre = equation[1]

    if genre == "horror":
        PORT = 5024
    elif genre == "comedy":
        PORT = 5026
    
    new_s = socket.socket()
    new_s.connect(("localhost", PORT))
    new_s.send(data.encode('utf-8'))
    result = new_s.recv(1024)
    new_s.close()

    cli.send(result)
    cli.close()

