import threading

import socket

sock = socket.socket()

sock.bind(('127.0.0.1',8001))
sock.listen(2)

def clientConn(conn):
	while True:
		conn.send("Connected".encode())
		data = conn.recv(1024).decode()
		print (data)

while True:
	conn, addr = sock.accept()
	threading.Thread(target=clientConn,args=(conn,)).start()

conn.close()
sock.close()