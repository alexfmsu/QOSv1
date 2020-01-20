from ElectronShell import ElectronShell

class Atom:
	id = 0

	def __init__(self, id=None, n_levels=2, electron_shell=None, pos=None):
		if id is None:
			self.id = Atom.id
			Atom.id += 1
		
		self.pos = pos

		self.n_levels = n_levels

		if electron_shell is not None:
			self.electron_shell = ElectronShell(electron_shell)


	def info(self):
		print('id:', self.id)
		print('n_levels:', self.n_levels)

		print('ElectronShell: ', end='')
		self.electron_shell.info()
		# print('spins:', self.spins)
