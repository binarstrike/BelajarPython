"""
def nama_fungsi() -> tipe data nilai return(int,float,None):
	pass
"""

def namaku() -> None:
	print("binar nugroho")

namaku()
# output: binar nugroho 

# deklarasi fungsi dengan parameter
def tambah(x, y) -> float:
	# nilai kembalian ↓
	return x + y;

z = tambah(6, 9)
print(z)
# output: 15

def xyz(*args) -> None:
	arg_len = len(args)
	for i in args:
		print(i)

xyz(8,9,5,6,3,1)
"""
output:
8
9
5
6
3
1
"""