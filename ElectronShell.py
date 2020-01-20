from Tools.Assert import Assert

class SubShell:
	def __init__(self, max_electrons):
		self.max_electrons = max_electrons
		# self.l = l

class ElectronShell:
	level = {
		'K': { 
			'1s': SubShell(max_electrons=2),
		},
		'L': { 
			'2s': SubShell(max_electrons=2),
			'2p': SubShell(max_electrons=6)
		},
		'M': { 
			'3s': SubShell(max_electrons=2),
			'3p': SubShell(max_electrons=6),
			'3d': SubShell(max_electrons=10)
		},
		'N': { 
			'4s': SubShell(max_electrons=2),
			'4p': SubShell(max_electrons=6),
			'4d': SubShell(max_electrons=10),
			'4f': SubShell(max_electrons=14)
		},
		'O': { 
			'5s': SubShell(max_electrons=2),
			'5p': SubShell(max_electrons=6),
			'5d': SubShell(max_electrons=10),
			'5e': SubShell(max_electrons=14),
			'5f': SubShell(max_electrons=18)
		}
	}

	def __init__(self, electron_shell):
		self.levels = {}

		for i in electron_shell:
			Assert(isinstance(i, tuple), 'i is not tuple')
			Assert(len(i) == 2, 'len(i) != 2')
			self.set_level(i[0], i[1])

	def set_level(self, id, spin):
		Assert(spin == 0 or spin == '0' or spin == 'up' or spin == 'down', 'incorrect spin')
		self.levels[id] = spin

	def unset_level(self, lvl):
		self.levels[id] = 0

	def info(self):
		print(self.levels)