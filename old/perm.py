from lib.Assert import Assert
from itertools import product

n_levels = 2
n_atoms = 3
capacity = 2


def basis(capacity, n_atoms, n_levels):
    l = []

    l.append(range(capacity + 1))

    for i in range(n_atoms):
        l.append(range(n_levels))

    kwargs = tuple(l)

    permutations = filter(lambda x: sum(x) <= capacity, product(*kwargs))

    return permutations


class Atom:
    atom_id = 0

    def __init__(self, id=None, n_levels=2):
        self.n_levels = n_levels
        self.shell = [''] * n_levels

        if id is None:
            self.id = Atom.atom_id
            Atom.atom_id += 1

    def set_shell(self, lvl, spin):
        Assert(lvl >= 0 and lvl < self.n_levels, "lvl < 0 or lvl >= self.n_levels")
        Assert(spin == 'up' or spin == 'down', "spin != 'up' and spin != 'down'")
        self.shell[lvl] = spin

    def print(self):
        print('n_levels:', self.n_levels)
        print('shell:', self.shell)
        print('id:', self.id)


def basis2(capacity1, capacity2, n1_atoms, n1_levels, n2_atoms, n2_levels):
    l = []

    l.append(range(capacity1 + 1))

    # shift = []
    # shift
    # l.append(range(capacity2 + 1))

    for i in range(n1_atoms):
        l.append(range(n1_levels))
    # for i in range(n2_atoms):
    #     l.append(range(n2_levels))

    kwargs = tuple(l)

    permutations = product(*kwargs)
    # permutations = filter(lambda x: x.count(1) == capacity1 and x.count(2) == capacity2, product(*kwargs))

    # p = []

    # for i in permutations:
    # p.append([(i[0], list(i[1:n1_atoms + 1])), (i[n1_atoms + 1], list(i[n1_atoms + 2:]))])
    # return p
    return permutations

capacity1 = 2
capacity2 = 2

n1_atoms = 3
n1_levels = 3

n2_atoms = 3
n2_levels = 3

# a = Atom()
# a.set_shell(0, 'u')
# a.print()

# a = Atom()
# a.print()


# def print_basis(id, n_atoms):
#     for i in range(n_atoms):
#         print(id & 1, end='')
#         id >>= 1

#     print()

# print_basis(1, 3)
b = basis2(capacity1, capacity2, n1_atoms, n1_levels, n2_atoms, n2_levels)


# b = [(i[0], list(i[1:2])) for i in b]
for i in b:
    print(i)
