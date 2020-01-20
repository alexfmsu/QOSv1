from Cavity import Cavity
from Atom import Atom
from ElectronShell import *

a0 = Atom(electron_shell=[(5, 0), (4,'up')])
a0.info()

ph = 2
cv = Cavity(wc=1, n_photons=2, wa=1, atoms=[])

cv.add_atom(a0)
cv.info()
# cv.remove_atom(a0)
# cv = Cavity(n_photons=2, atoms=[a0])
cv.info()

# a1 = Atom()
# a1.info()


# e = ElectronShell()

# print(ElectronShell.level)
# print(ElectronShell.level['K']['1s'].max_electrons)

