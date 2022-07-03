#pylint:disable=W0611
import socket
import os, sys

HOST, PORT, PLAYERNAME = str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3])

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as player:
		player.connect((HOST, PORT))
		while True:
			data_recv = player.recv(1024)
			print('Received data : ', data_recv.decode("utf-8"))
			if data_recv.decode('utf-8') in ('q', 'quit', 'close'):
				print('Connection Closed'); sys.exit()

if __name__ == '__main__':
	main()