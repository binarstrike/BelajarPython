#pylint:disable=W0611
import socket as sck

HOST = '192.168.43.1'
PORT = 1111

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
	client.connect((HOST, PORT))
	#client.sendall(b'Test Client')
	data = client.recv(1024)
print('Data diterima -> ', repr(data))