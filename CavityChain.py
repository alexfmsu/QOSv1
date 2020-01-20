from Tools.Assert import Assert
from Tools.Print import cprint

class CavityChain:
	def __init__(self, cavities):
		Assert(isinstance(cavities, list), 'cavities is not list')
		self.cavities = cavities

	def add_cavity(self, cavity):
		self.cavities.append(cavity)
	
	def info(self):
		for cv in self.cavities:
			cv.info()
