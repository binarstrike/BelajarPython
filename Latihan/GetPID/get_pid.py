import os

def main():
	try:
		PKGNAME = input('Package Name -> ')
		os.system('pidof %s' % PKGNAME)
	except:
		print('No such Proccess')
if __name__ == '__main__':
	main()