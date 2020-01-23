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
# from QOS.State import State
from QOS.BaseStates import BaseStates


def subsets(x, indices):
    y = []

    for i in indices:
        y += list(x[i[0]:i[1]])

    return y


class Hamiltonian(Matrix):

    def __init__(self, cavity_chain):
        # self.capacity = cavity_chain.capacity
        self.cavity_chain = cavity_chain

        # self.set_basis()
        # self.size = len(self.basis)
        # self.size = len(self.states)
        # H0 = self.H0(cavity_chain)

        # self.H = H0

    def print(self):
        print(self.H.data.todense())

    def print_states(self):
        n_digits = len(str(self.size))
        print_format = ''.join(['%', str(n_digits), 'd'])

        for k, v in self.states.items():
            print(print_format % k, ': ', v, sep='')

    # -----------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------- H0 ---------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    def H0(self, cavity_chain):
        pass
        H0 = lil_matrix((self.size, self.size))
        self.H0_symb = lil_matrix((self.size, self.size), dtype=str)

        for i in range(len(self.states)):
            for j in range(len(self.states)):
                self.H0_symb[i, j] = ''

        for i in range(len(self.states)):
            # cnt = 0

            state_i = self.states[i]

            H0[i, i] = 0

            for cv_i, cavity in cavity_chain.cavities.items():
                for ph_type, v_wc in cavity.wc.items():
                    # print(cv_i)
                    # print(k)
                    # print(self.states[i][cv_i])
                    # print(state_i)
                    # print('cv_i=', cv_i)
                    # print(state_i[cv_i])
                    # H0[i, i] = state_i[cv_i][0][ph_type]
                    H0[i, i] += v_wc['value'] * self.states[i][cv_i][0][ph_type]
                    print(H0[i, i])
                    # H0[i, i] = cavity.wc[k]['value'] * self.states[i][cv_i][k]

                    # k_ = k.replace('<->', '')
                    # print('k:', k_)
                    # exit(0)
                    # self.H0_symb[i, i] = ab(self.H0_symb[i, i], 'wc' + sub(k_), self.states[i]['ph'][cnt])

                    # cnt += 1

                # for atoms in cavity.atoms:
                #     H0[i, i] += v_wc['value'] * state_i[cv_i][0][ph_type]

        # return H0
        return Matrix(m=self.size, n=self.size, dtype=np.float, data=H0)
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
# =====================================================================================================================
    # def set_basis2(self):
    #     l = []

    #     shift = []

    #     # print(self.cavity_chain.cavities)
    #     for cavity in self.cavity_chain.cavities.values():
    #         for capacity in self.capacity:
    #             # ph_range = list(range(len(cavity.wc)))
    #             ph_range = list(range(capacity['value'] + 1))
    #             l.append(ph_range)
    #         # print(l)
    #         # exit(0)
    #         # print(cavity)
    #         for atom in cavity.atoms:
    #             at_range = list(range(atom.n_levels()))
    #             l.append(at_range)
    #     # exit(0)
    #     kwargs = tuple(l)
    #     permutations = product(*kwargs)
    #     # permutations = filter(lambda x: x.count(1) == capacity1 and x.count(2) == capacity2, product(*kwargs))
    #     # print('print1')
    #     # for i in permutations:
    #     #     print(i)
    #     # exit()
    #     permutations = list(permutations)

    #     # permutations = list(filter(lambda x: x.count(1) >= 0, permutations))
    #     print('print11')
    #     for i in permutations:
    #         print(i)

    #     # for capacity in self.cavity_chain.capacity:
    #     #     # print(capacity['levels'][1], '=', capacity['value'])
    #     #     # permutations = list(filter(lambda x: x.count(1) > 0, tuple(permutations)))
    #     #     permutations = list(filter(lambda x: x.count(capacity['levels'][
    #     #                         1]) == capacity['value'], tuple(permutations)))
    #     #     print('print2')
    #     #     for i in permutations:
    #     #         print(i)
    #     #     # permutations = filter(lambda x: x.count(capacity['levels'][1]) == capacity['value'], product(*kwargs))
    #     #     # break
    #     # permutations = list(permutations)
    #     # print('print3')

    #     # for i in permutations:
    #     #     print(i)
    #     # exit(0)

    #     self.states = {}
    #     ph_counts = {}
    #     for i in self.cavity_chain.capacity:
    #         ph_counts[i['notation']] = {0}
    #     print(ph_counts)
    #     state_num = 0
    #     for i in permutations:
    #         shift = 0

    #         state_i = tuple()
    #         # print(1)
    #         ind = 0
    #         for cavity in self.cavity_chain.cavities.values():
    #             photons = i[shift: shift + len(cavity.wc)]
    #             cv_state = []
    #             # print(cavity.wc)
    #             # print(photons)

    #             for k, v in enumerate(cavity.wc):
    #                 print(photons)
    #                 ph_counts[v['notation']] += photons[k]
    #                 # print(k)
    #                 cv_state.append({v['notation']: photons[k]})
    #                 # cv_state.append({v['notation']: photons[k]})
    #             # print(photons[1])
    #             # exit(0)
    #             # list(photons)
    #             # cv_state = list(photons)
    #             shift += len(cavity.wc)

    #             atoms = i[shift: shift + cavity.get_n_atoms()]
    #             cv_state += [list(atoms)]
    #             shift += cavity.get_n_atoms()

    #             state_i += (cv_state,)

    #         self.states[state_num] = state_i
    #         state_num += 1
    #         # print('state_i:', state_i)
# =====================================================================================================================
    # def set_basis(self):
    #     cavities = list(self.cavity_chain.cavities.values())

    #     self.base_states = {}
    #     base_states_cnt = 0

    #     state = self.cavity_chain.get_state()
    #     code = flat_list(state)
    #     code = ''.join(map(str, code))
    #     # print(state)
    #     # print('code:', code)
    #     # exit(0)
    #     self.base_states = {}
    #     self.base_states_checked = {}
    #     self.base_states_not_checked = {}
    #     self.base_states_not_checked[code] = state

    #     # self.base_states.append(self.cavity_chain.state)
    #     print(self.base_states)

    #     while len(self.base_states_not_checked):
    #         keys = self.base_states_not_checked.keys()
    #         keys = list(keys)
    #         # print(list(keys))
    #         # print(keys[0])
    #         # exit(0)
    #         state = self.base_states_not_checked[keys[0]]
    #         code = flat_list(state)
    #         code = ''.join(map(str, code))

    #         for cv_k, cv_v in self.cavity_chain.cavities.items():
    #             # print('cv_', cv_k)
    #             # print(state)
    #             photons = state[cv_k][0]
    #             atoms = state[cv_k][1]
    #             wc = cv_v.wc

    #             for ph_type, ph_cnt in photons.items():
    #                 for k_atom, v_atom in enumerate(atoms):
    #                     # lvl = v_atom.lvl
    #                     # print(v_atom)
    #                     lvl = state[cv_k][1][k_atom]
    #                     n_levels = cv_v.atoms[k_atom].n_levels()

    #                     ph_from = wc[ph_type]['levels'][0]
    #                     ph_to = wc[ph_type]['levels'][1]

    #                     # print(photons)
    #                     # print('ph_type', ph_type)
    #                     # print('ph_type', photons[ph_type])

    #                     # from cavity -> to atom
    #                     new_state = None

    #                     if photons[ph_type] > 0:
    #                         if cv_k == 1 and ph_from == 1:
    #                             print('lvl=', lvl, 'ph_from=', k_atom, ph_from, state)
    #                         if lvl == ph_from:
    #                             # print(4)
    #                             # exit(0)
    #                             new_state = deepcopy(state)
    #                             new_state[cv_k][0][ph_type] -= 1
    #                             new_state[cv_k][1][k_atom] += 1
    #                     else:
    #                         if lvl == ph_to:
    #                             new_state = deepcopy(state)
    #                             new_state[cv_k][0][ph_type] += 1
    #                             new_state[cv_k][1][k_atom] -= 1

    #                     if new_state is not None:
    #                         newcode = flat_list(new_state)
    #                         newcode = ''.join(map(str, newcode))

    #                         if newcode not in self.base_states and newcode not in self.base_states_not_checked:
    #                             self.base_states_not_checked[newcode] = new_state

    #                             print('new_state:', newcode, new_state)

    #         # print('del', code)
    #         del self.base_states_not_checked[code]
    #         self.base_states[code] = state
    #         # print('-' * 100, end='\n')

    #         # for i in self.base_states_not_checked:
    #         #     print(i)
    #         # print('-' * 100, end='\n')
    #         # for i in self.base_states:
    #         #     print(i)
    #         # print('-' * 100, end='\n\n')

    #     for i in self.base_states:
    #         print(i)
    #     print()
    #     for i in self.base_states_not_checked:
    #         print(i)
    #     print()
    #     for i in self.base_states_checked:
    #         print(i)
    #     # print(1)
    #     exit(0)
    #     pass
    #     l = []

    #     local_jumps = [cavity.jumps for cavity in self.cavity_chain.cavities.values()]

    #     shift = 0
    #     ph_ind = {}
    #     at_ind = []

    #     for k, v in enumerate(local_jumps):
    #         for ph_type in v:
    #             ph_range = list(range(self.cavity_chain.capacity[ph_type]['value'] + 1))
    #             l.append(ph_range)

    #             if ph_type not in ph_ind:
    #                 ph_ind[ph_type] = []

    #             ph_ind[ph_type].append(shift)
    #             shift += 1

    #         for atom in self.cavity_chain.cavities[k].atoms:
    #             at_range = list(range(atom.n_levels()))
    #             l.append(at_range)

    #         at_ind.append([shift, shift + len(self.cavity_chain.cavities[k].atoms)])
    #         shift += len(self.cavity_chain.cavities[k].atoms)

    #     expr_list = []

    #     for ph_type, ph_pos in ph_ind.items():
    #         lvl_2 = self.cavity_chain.capacity[ph_type]['levels'][1]

    #         expr = 'np.array(x)[' + str(ph_pos) + '].sum() + subsets(x, ' + str(at_ind) + ').count(' + str(lvl_2) + ') == ' + \
    #             str(self.cavity_chain.capacity[ph_type]['value'])

    #         expr_list.append(expr)

    #     expr = ' and '.join(expr_list)
    #     # print(expr)

    #     kwargs = tuple(l)
    #     permutations = product(*kwargs)

    #     permutations = filter(lambda x: eval(expr), product(*kwargs))
    #     # permutations = filter(lambda x: np.array(x)[[0, 3]].sum() + x.count(1) == 3, product(*kwargs))

    #     permutations = list(permutations)

    #     self.states = {}
    #     for i in range(len(permutations)):
    #         shift = 0

    #         state_i = tuple()

    #         for cv_i, cv in self.cavity_chain.cavities.items():
    #             # cv_state = []
    #             cv_state_ph = {}

    #             for j in local_jumps[cv_i]:
    #                 ph_type = j
    #                 ph_state = permutations[i][shift]

    #                 cv_state_ph[ph_type] = ph_state
    #                 shift += 1

    #             n_atoms = cv.get_n_atoms()

    #             at_state = permutations[i][shift:shift + n_atoms]
    #             cv_state = [cv_state_ph, list(at_state)]

    #             shift += n_atoms

    #             state_i += (cv_state,)

    #         self.states[i] = state_i
# =====================================================================================================================
