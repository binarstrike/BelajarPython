def tambah(x, y) -> float:
	return x + y

def kurang(x, y) -> float:
	return x - y

def kali(x, y) -> float:
	return x * y

def pangkat(x, pangkat=1) -> float:
	return x ** pangkat

def bagi(x, y) -> float:
	if (x, y) == 0 or x < 1 or y < 1:
		print("tidak bisa membagi dengan bilangan bernilai 0 dan negatif")
		return
	else:
		return x / y