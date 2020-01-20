from Tools.Print import *

class Cavity:
	def __init__(self, wc, n_photons, wa, atoms):
		self.n_photons = n_photons
		self.atoms = {}

		for atom in atoms:
			self.atoms[atom.id] = atom

	def add_photon(self):
		pass

	def remove_photon(self):
		pass

	def add_atom(self, atom):
		self.atoms[atom.id] = atom

	def move_atom(self, atom, pos):
		pass
		# if atom in self.atoms:
			# self.atoms[]
	def remove_atom(self, atom):
		if atom in self.atoms:
			del self.atoms[atom.id]

	def info(self):
		cprint('n_photoms: ', color='green', attrs=['bold'], end='')
		print(self.n_photons, end='\n\n')

		cprint('Atoms:', color='green', attrs=['bold'])
		for atom in self.atoms.values():
			atom.info()

		print()