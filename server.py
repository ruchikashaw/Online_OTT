import socket
import json

s = socket.socket()    
print('Socket is created')

s.bind(("localhost",9999))      

s.listen(10)           
print("Waiting for connection")   

cli,addr = s.accept()
while True:
    

    msg ='' 
    data = cli.recv(1024)
    msg = data.decode('utf-8')

    if msg == 'Over':
        print("Connection over")
        break
    
    result = " "
    equation = msg.split(" ")
    language = equation[0]
    PORT = None
    print(language)
    if language == "english":
        PORT = 5021
    elif language == "bengali":
        PORT = 5022
    elif language == "hindi":
        PORT = 5023
    
    if PORT:
        print(PORT)
        new_s = socket.socket()
        new_s.connect(("localhost", PORT))
        new_s.send(msg.encode('utf-8'))
        result = new_s.recv(1024)
        new_s.close()

        cli.send(result)
    else: 
        wr = "Enter correct language"
        cli.send(wr.encode('utf-8'))

cli.close()
s.close()
