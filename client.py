import socket


client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)

client.connect(("localhost", 9999))

while True:
	
	inp = input("Enter the language you would like to see and the genre you would like to prefer: ")
	if inp == "Over":
		break
	
	
	client.send(inp.encode())

	
	answer = client.recv(1024)
	print(answer.decode())
	print("Type 'Over' to terminate")

client.close()