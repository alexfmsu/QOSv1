# =================================================== DESCRIPTION =====================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== DESCRIPTION =====================================================


# =================================================== EXAMPLES ========================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== EXAMPLES ========================================================


# =====================================================================================================================
# utils
from utils.ParseJumps import parse_jumps
# =====================================================================================================================


class CavityChain:
    __slots__ = ['capacity', 'cavities', 'n_cavities', 'jumps', '__connections']

    def __init__(self, capacity, cavities):
        Assert(isinstance(cavities, list), 'cavities is not list')

        self.capacity = parse_jumps(capacity)
        print(self.capacity)
        # exit(0)
        self.cavities = {}
        self.n_cavities = 0
        self.__connections = {}

        for i in range(len(cavities)):
            self.cavities[i] = cavities[i]
            self.n_cavities += 1

        self.jumps = self.capacity.keys()

        for cavity in cavities:
            Assert(not(cavity.jumps - self.jumps), 'cavity.jumps - self.jumps')

    def connect(self, cavity_id1, cavity_id2, mu):
        cvs = sorted([cavity_id1, cavity_id2])

        self.__connections[str(cvs[0]) + '<->' + str(cvs[1])] = {
            'amplitude': mu,
            'cavity_ids': cvs,
        }

    def print_connections(self):
        for cvs, mu in self.__connections.items():
            print(cvs, ': ', to_Hz(mu['amplitude']), sep='')

    def add_cavity(self, cavity):
        self.cavities.append(cavity)

        self.n_cavities += 1

    def get_state(self):
        state = ()

        for cv_k, cv_v in self.cavities.items():
            state += (cv_v.get_state(),)

        return state

    def print_state(self):
        for cv_k, cv_v in self.cavities.items():
            cv_v.print_state()

    def info(self, mode=None):
        json_data = {}
        json_data['Capacity'] = {}

        for k, v in self.capacity.items():
            json_data['Capacity'][k] = v['value']

        for cavity in self.cavities.values():
            json_data['Cavity_' + str(cavity.get_id())] = cavity.json_data(mode)

        if self.__connections:
            json_data['Connections'] = {}

            for conn_k, conn_v in self.__connections.items():
                # print(conn_v)
                # exit(0)
                conn_type = 'Cavity_' + str(conn_v['cavity_ids'][0]) + '<->' + 'Cavity_' + str(conn_v['cavity_ids'][1])
                json_data['Connections'][conn_type] = to_Hz(conn_v['amplitude'])
                # print(cvs, ': ', to_Hz(mu), sep='')

        json_formatted_str = json.dumps(json_data, indent=4)

        colorful_json = highlight(json_formatted_str, lexers.JsonLexer(), formatters.TerminalFormatter())

        print(colorful_json)
