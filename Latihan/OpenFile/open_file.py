def main():
	file = open('file.txt','w+')
	file.write('Hello, world!!')
	file.close()
	file = open('file.txt', 'r')
	print(file.read())
	file.close()
if __name__ == '__main__':
	main()