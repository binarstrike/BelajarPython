from tkinter import  Tk, mainloop, Label
from time import strftime

Root = Tk()
Root.title('Clock')

def time():
	clock = strftime('%H:%M:%S %p')
	label.config(text=clock)
	label.after(1001-1, time)

label = Label(Root, font=('digital-7 (mono).ttf', 20), background='black', foreground='cyan')
label.pack()
time()

mainloop()