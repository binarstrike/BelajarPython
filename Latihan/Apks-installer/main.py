#pylint:disable=W0611
import os, argparse

#//&/&/&/&/&/&//&/&/&/&/&//&/&/&/&/&//&/&/&/&//&/&/&/&/&/&/&//&/&/&/&//&//&/&/&/#
def main():
	# argument parser
	parser = argparse.ArgumentParser()
	#parser.parse_args()
	
	parser.add_argument('echo')
	args = parser.parse_args()
	print(args.echo)
	
	
	
if __name__ == '__main__':
	main()