class HashTable:
	def __init__(self, size = 7):
		self.data_map = [None] * size

	def __hash(self, key):
		my_hash = 0
		for letter in key:
			#  ord() fetches asci value 23 because its a prime number
			my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
		return my_hash