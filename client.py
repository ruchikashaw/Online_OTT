import socket
import json


client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)

client.connect(("localhost", 9999))

while True:
	
	inp = input("Enter the language you would like to see and the genre you would like to prefer (Sample Input: English Comedy): \n>")
	if inp.lower() == "Over":
		break
	
	client.send(inp.lower().encode())
	
	answer = client.recv(1024)
	res = json.loads(answer.decode())
	for mov in res:
		print("---------------\nMovie Name: {}\nYear Released: {}\nRating: {}\n---------------".format(mov["Title"], mov["Released"], mov["Rating"]))

	print("Type 'Over' to terminate")

client.close()