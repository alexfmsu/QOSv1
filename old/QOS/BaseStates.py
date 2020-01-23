import re


class BaseStates:

    def __init__(self, states):
        self.states = {}

        for k, v in enumerate(sorted(states)):
            self.states[k] = states[v]

    def print(self, mode='short'):
        print('BaseStates:', color="green")

        n_states = len(self.states)
        n_digits = len(str(n_states))
        print_format = ''.join(['%', str(n_digits), 'd'])

        if mode == 'string':
            for k, v in self.states.items():
                print(print_format % k, ': ', v.as_string(), sep='')
        elif mode == 'array':
            for k, v in self.states.items():
                print(print_format % k, ': ', v.as_array(), sep='')
        elif mode == 'braket':
            for k, v in self.states.items():
                print(print_format % k, ': ', v.as_braket(), sep='')
        elif mode == 'raw':
            for k, v in self.states.items():
                print(print_format % k, ': ', v.state, sep='')
        elif mode == 'short':
            for k, v in self.states.items():
                l = []

                for cv in v.state:
                    cv[0] = {str(ph_v) + str(sub(ph_k.replace('<->', ''))) for ph_k, ph_v in cv[0].items()}
                    cv = str(tuple(cv))
                    cv = cv.replace('\'', '')
                    cv = cv.replace('{', '')
                    cv = cv.replace('}', '')

                    l.append(cv)

                print(print_format % k, ': ', ' ⊗  '.join(l), sep='')
