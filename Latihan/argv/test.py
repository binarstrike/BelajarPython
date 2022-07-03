from sys import  argv


def main():
	for argc in range(1,10):
		if '-p' in argv[argc]:
			print("-> %s" % argv[argc+1])
			break
	
if __name__ == '__main__':
	main()