from QOS.BaseStates import BaseStates
from QOS.State import State
from QOS.Hamiltonian import Hamiltonian
from copy import deepcopy
from math import sqrt


class QuantumSystem:
    __slots__ = [
        '__cavity_chain', '__cavities',
        '__hamiltonian',
        '__base_states',
        '__wavefunction',
        '__densitymatrix',
        'base_states'
    ]

    def __init__(self, cavity_chain=None):
        self.__cavity_chain = cavity_chain
        self.__cavities = cavity_chain.cavities

        if self.__cavity_chain is not None:
            self.__base_states = self.set_basis()
            self.__hamiltonian = Hamiltonian(self.__base_states, self.__cavity_chain)
            # self.__base_states = self.__hamiltonian.states
            # self.__wavefunction = None
            # self.__densitymatrix = None

    def get_cavity_chain(self):
        return self.__cavity_chain

    def set_cavity_chain(self, cavity_chain):
        self.__cavity_chain = cavity_chain

    def print_base_states(self, mode='short'):
        self.__base_states.print(mode)
        # for k, v in self.__base_states.items():
        #     v.info('-v')

    def set_basis(self):
        cv_chain = self.__cavity_chain
        cavities = list(self.__cavities.values())

        state = State(state=cv_chain.get_state())
        notation = state.as_string()
        # print(state)
        # print('code:', code)
        # exit(0)

        base_states = {}
        base_states_not_checked = {notation: state}

        while len(base_states_not_checked):
            keys = base_states_not_checked.keys()
            keys = list(keys)

            state = base_states_not_checked[keys[0]]
            notation = state.as_string()

            for cv_k, cv_v in self.__cavities.items():
                # print('cv_', cv_k)
                # print(state)
                photons = state.state[cv_k][0]
                atoms = state.state[cv_k][1]
                wc = cv_v.wc

                for ph_type, ph_cnt in photons.items():
                    for k_atom, v_atom in enumerate(atoms):
                        # lvl = v_atom.lvl
                        # print(v_atom)
                        lvl = state.state[cv_k][1][k_atom]
                        n_levels = cv_v.atoms[k_atom].n_levels()

                        ph_from = wc[ph_type]['levels'][0]
                        ph_to = wc[ph_type]['levels'][1]

                        # print(photons)
                        # print('ph_type', ph_type)
                        # print('ph_type', photons[ph_type])

                        # from cavity -> to atom
                        new_state = None

                        if photons[ph_type] > 0:
                            # if cv_k == 1 and ph_from == 1:
                                # print('lvl=', lvl, 'ph_from=', k_atom, ph_from, state)
                            if lvl == ph_from:
                                # print(4)
                                # exit(0)
                                # print(55)
                                new_state = deepcopy(state.state)
                                # print(66)
                                amplitude = sqrt(ph_to) * cv_v.atoms[k_atom].g[ph_type]['value']
                                new_state[cv_k][0][ph_type] -= 1
                                new_state[cv_k][1][k_atom] += 1
                        else:
                            if lvl == ph_to:
                                new_state = deepcopy(state.state)
                                amplitude = sqrt(ph_to) * cv_v.atoms[k_atom].g[ph_type]['value']
                                new_state[cv_k][0][ph_type] += 1
                                new_state[cv_k][1][k_atom] -= 1
                                amplitude = cv_v.atoms[k_atom].g[ph_type]['value']

                        if new_state is not None:
                            newcode = State.string_notation(new_state)
                            # newcode = State.flat_list2(new_state)
                            # print(newcode)
                            # exit(0)
                            # newcode = ''.join(map(str, newcode))

                            # newcode = new_state.as_string()
                            if (newcode not in base_states) and (newcode not in base_states_not_checked):
                                new_state = State(state=new_state)

                                base_states_not_checked[newcode] = new_state

                                # amplitude = to_Hz(amplitude)
                                # print((state.get_id(), new_state.get_id()), (new_state.get_id(), state.get_id()))

                                new_state.connect(state=state, amplitude=amplitude)
                                state.connect(state=new_state, amplitude=amplitude)

                                # if state.get_id() == 0 and new_state.get_id() == 4:
                                #     new_state.info('-v')
                                #     exit(0)
                                print('new_state:', newcode)

            del base_states_not_checked[notation]
            base_states[notation] = state

        for k, v in base_states.items():
            v.info('-v')
        Assert(len(base_states_not_checked) == 0, 'len(self.base_states_not_checked) != 0')

        return BaseStates(base_states)
