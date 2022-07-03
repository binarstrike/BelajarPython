#pylint:disable=W0611
import socket
import os, sys
from _thread import start_new_thread

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
player = {
	'one' : {
		'host' : '',
		'port' : ''
	},
	'two' : {
		'host' : '',
		'port' : ''
	}
}

def handle_client(client):
	conn, addr = client.accept()
	if player['one']['host'] == '':
		player['one']['host'] = addr[0]
		player['one']['port'] = addr[1]

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		server.bind((HOST, PORT))
		server.listen()
		conn, addr = server.accept()
		with conn:
			print(f'Connected Client with IP {addr[0]} PORT {addr[1]}')
			while True:
				send_data = str(input('- > '))
				conn.sendto(str.encode(send_data), addr)
				if send_data in ('q', 'quit', 'close'):
					conn.close()
					sys.exit()

if __name__ == '__main__':
	main()