# =================================================== DESCRIPTION =====================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== DESCRIPTION =====================================================


# =================================================== EXAMPLES ========================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== EXAMPLES ========================================================


# =====================================================================================================================
# system
from itertools import product
from copy import deepcopy
# =====================================================================================================================
# scientific
import numpy as np
from scipy.sparse import identity, kron, eye, csc_matrix, bsr_matrix, lil_matrix
# =====================================================================================================================
# libs
from lib.Matrix import Matrix
# =====================================================================================================================
# utils
from utils.flat_list import flat_list
# =====================================================================================================================
from QOS.BaseStates import BaseStates


def subsets(x, indices):
    y = []

    for i in indices:
        y += list(x[i[0]:i[1]])

    return y


class Hamiltonian(Matrix):

    def __init__(self, base_states, cavity_chain):
        self.__base_states = base_states
        self.size = len(base_states.states)
        # self.capacity = cavity_chain.capacity
        self.cavity_chain = cavity_chain

        # self.set_basis()
        # self.size = len(self.basis)
        # self.size = len(self.states)
        H0 = self.H0(base_states)
        HI = self.HI(base_states)

        self.H = H0 + HI

        self.print()

    def print(self):
        print(self.H.data.todense())

    def print_states(self):
        n_digits = len(str(self.size))
        print_format = ''.join(['%', str(n_digits), 'd'])

        for k, v in self.states.items():
            print(print_format % k, ': ', v, sep='')

    # -----------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------- HI ---------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    def H0(self, cavity_chain):
        H0 = lil_matrix((self.size, self.size))
        self.H0_symb = lil_matrix((self.size, self.size), dtype=str)

        cavities = self.cavity_chain.cavities
        # print(self.__base_states.states)
        for k, v in self.__base_states.states.items():
            id_from = k

            H0[k, k] = 0

            for cv in v.state:
                photons = cv[0]
                atoms = cv[1]

                for ph_type, ph_count in photons.items():
                    wc = cavities[0].wc[ph_type]['value']
                    H0[k, k] += wc * ph_count
                    # print(cavities[0].wc[ph_type]['value'])

                for i, atom_lvl in enumerate(atoms):
                    wa = cavities[0].atoms[i].wa['0<->1']['value']
                    H0[k, k] += wa * atom_lvl

        # return H0
        return Matrix(m=self.size, n=self.size, dtype=np.float, data=H0)
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------- HI ---------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    def HI(self, cavity_chain):
        HI = lil_matrix((self.size, self.size))
        # self.H0_symb = lil_matrix((self.size, self.size), dtype=str)
        # print('-' * 100)

        base_states = self.__base_states.states
        # print(self.__base_states.states)
        for k, v in base_states.items():
            id_from = k
            # print(k, v.connections)
            # v.info('-v')
            for conn in v.connections:
                # print(conn)
                # conn['state'].info('-v')
                other_id = conn['state'].get_id()

                key_to = self.__base_states.key_by_id(other_id)
                # print(base_states.keys())
                # id_to = list(base_states.keys())[list(base_states.values()).index(other_id)]
                # id_to = conn['to']
                # id_to = conn['state'].get_id() ?
                amplitude = conn['amplitude']
                print('id_from:', id_from, '-> id_to:', key_to, ', ampl:', amplitude, sep='')
                # exit(0)
                HI[id_from, key_to] = amplitude

        # return H0
        return Matrix(m=self.size, n=self.size, dtype=np.float, data=HI)
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
# =====================================================================================================================
