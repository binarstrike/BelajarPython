import curses, time



def ask(q):
	inp = str(input(f"\n{q} -> "))
	if inp in ('y','Y'):
		return True
	else: return False
	

def main():
	screen = curses.initscr()
	screen.getch()
	curses.endwin()
if __name__ == '__main__':
	main()