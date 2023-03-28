import socket

s = socket.socket()    
print('Socket is created')

s.bind(("localhost",9999))      

s.listen(10)           
print("Waiting for connection")
cli,addr = s.accept()

msg =''    

while True:
    data = cli.recv(1024)
    msg = data.decode('utf-8')

    if msg == 'Over':
        print("Connection over")
        break
    
    result = " "
    equation = msg.split(" ")
    language = equation[0]
    print(language)
    if language == "English":
        PORT = 5021
    elif language == "Bengali":
        PORT = 5022
    elif language == "Hindi":
        PORT = 5023
   
    print(PORT)
    new_s = socket.socket()
    new_s.connect(("localhost", PORT))
    new_s.send(msg.encode('utf-8'))
    result = new_s.recv(1024)
    new_s.close()

    cli.send(result)

cli.close()
s.close()
