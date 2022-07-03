#pylint:disable=C0303
#pylint:disable=W0611
#pylint:disable=C0116
#pylint:disable=C0304
#pylint:disable=C0114
import random as rd
import os, time, sys
BATU = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
GUNTING = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
KERTAS = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

batu,gunting,kertas = 1,2,3

def main():
	os.system('clear')
	bgt = ['blank',BATU,GUNTING,KERTAS]
	input_user = int(input('Masukan Pilihan\n1.batu 2.gunting 3.kertas : '))
	if input_user not in range(1, 4):
		print('\nInput Masukan Salah')
		#os.system('sleep 2 && clear')
		time.sleep(2)
		os.system('clear')
		main()
	user_pil = bgt[input_user]
	print('Kamu Memilih : %s' % user_pil)
	# Computer ↓↓↓↓
	input_comp = rd.randint(1, 3)
	comp_pil = bgt[input_comp]
	print('Komputer Memilih : %s' % comp_pil)
	if input_user == input_comp:
		print('Seri')
	if input_user == batu and input_comp == gunting:
		print('Kamu Menang!!')
	if input_user == gunting and input_comp == batu:
		print('Kamu Kalah!!')
	if input_user == batu and input_comp == kertas:
		print('Kamu Kalah!!')
	if input_user == kertas and input_comp == batu:
		print('Kamu Menang!!')
	if input_user == kertas and input_comp == gunting:
		print('Kamu Kalah!!')
	if input_user == gunting and input_comp == kertas:
		print('Kamu Menang!!')
	new_game = input('Main Lagi? y/n : ')
	if new_game in ('y', 'Y'):
		main()
if __name__ == '__main__':
	main()