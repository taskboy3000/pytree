class TreeElement:
	def __init__(self, k, v):
		self.key = k
		self.value = v
		
	def compare (self, other):
		if (other == None):
			return 1
			
		if (self.key > other.key):
			return 1
			
		if (other.key > self.key):
			return -1
			
		# Must be equal
		return 0

	def __str__(self):
		return "TreeElement: Key=" + str(self.key) + "; Value=" + str(self.value)

