class Hamiltonian:
	def __init__(self, capacity, cavity_chain):
		self.capacity = capacity
		self.cavity_chain = cavity_chain

	# def set_basis(self, capacity1, capacity2, n1_atoms, n1_levels, n2_atoms, n2_levels):
	# 	l = []

	# 	l.append(range(capacity1+1))
	# 	l.append(range(capacity2+1))

	# 	for i in range(n1_atoms):
	# 		l.append(range(n1_levels))
	# 	for i in range(n2_atoms):
	# 		l.append(range(n2_levels))

	# 	kwargs = tuple(l)

	# 	permutations = filter(lambda x: x.count(1)==capacity1 and x.count(2)==capacity2, product(*kwargs))

	# 	p = []

	# 	for i in permutations:
	# 		p.append([(i[0], list(i[1:n1_atoms+1])), (i[n1_atoms+1], list(i[n1_atoms+2:]))])
	# 	return p
