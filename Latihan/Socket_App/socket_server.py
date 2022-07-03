#pylint:disable=W0611
import socket as sck

HOST = '192.168.43.1'
PORT = 1111

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
	server.bind((HOST, PORT))
	server.listen()
	connect, address = server.accept()
	with connect:
		print('Connected -> ', address)
		while True:
			data = server.recv(1024)
			if not data:
				break
			connect.sendall(data)