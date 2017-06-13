import socket

sock = socket.socket()

sock.connect(('localhost',8001))

while True:
	data = sock.recv(1024).decode()
	print (data)
	data_sen = input("Message >> ")
	sock.send(data_sen.encode())
sock.close()