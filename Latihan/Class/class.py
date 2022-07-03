#pylint:disable=W0105
class Hero:
	def __init__(self, nama):
		self.nama = nama
		self.attack = 0
		self.defense = 0
		self.mana = 0
	def add_attack(self, attack):
		self.attack += attack
		"""	/**/	"""
	def add_defense(self, defense):
		self.defense += defense
		"""	/**/	"""
	def add_mana(self, mana):
		self.mana += mana
		"""	/**/	"""
	def display_all(self):
		print("Nama Hero:", self.nama)
		print("Attack Power:", self.attack)
		print("Defense Power:", self.defense)
		print("Mana:", self.mana)
		"""	/**/	"""

def main():
	hero1 = Hero('Miya')
	hero1.add_attack(120)
	hero1.add_defense(75)
	hero1.add_mana(45)
	hero1.display_all()
	print("")
	hero2 = Hero("Zilong")
	hero2.add_attack(9999)
	hero2.add_defense(567)
	hero2.add_mana(344)
	hero2.display_all()

if __name__ == '__main__':
	main()