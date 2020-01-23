# =====================================================================================================================
# utils
from utils.flat_list import flat_list
# =====================================================================================================================


class State:

    @staticmethod
    def array_notation(raw_notation):
        return flat_list(raw_notation)

    @staticmethod
    def string_notation(raw_notation):
        return ''.join(map(str, State.array_notation(raw_notation)))

    @staticmethod
    def flat_list2(nestedList):
        atoms_flag = False
        tensor_flag = False

        s = ''
        flatList = []

        for elem in nestedList:
            if isinstance(elem, list):
                if atoms_flag:
                    s += '|'
                s += State.flat_list2(elem)

                if atoms_flag:
                    s += '〉'

                atoms_flag = False
                tensor_flag = True

            elif isinstance(elem, dict):
                s += '|'

                for v in elem.values():
                    s += str(v)
                s += '〉'

                atoms_flag = True

            else:
                s += str(elem)

        return s

    __ID = 0

    __slots__ = ['__id', '__byte_array', '__braket', 'connections', 'state', '__string']

    def __init__(self, state):
        self.__id = State.__ID
        State.__ID += 1
        print('id:', self.__id)
        self.state = state

        self.__byte_array = flat_list(self.state)
        # self.__string = ''.join(map(str, self.__byte_array))
        self.__string = State.string_notation(self.state)

        self.__braket = State.flat_list2(self.state)

        self.connections = []

    def as_string(self):
        return self.__string

    def as_array(self):
        return self.__byte_array

    def as_braket(self):
        return self.__braket

    def connect(self, state, amplitude):
        self.connections.append({'state': state, 'amplitude': amplitude})

    def json_data(self, mode=None):
        json_data = {}

        if mode == '-v':
            json_data['id'] = self.__id

            json_data['as_braket'] = self.as_braket()
            json_data['as_array'] = str(self.as_array())
            json_data['as_string'] = str(self.as_string())

            json_data['connections'] = []

            for i in self.connections:
                json_data['connections'].append({
                    'to': i['state'].__id,
                    'as_braket': i['state'].as_braket(),
                    'as_array': str(i['state'].as_array()),
                    'as_string': i['state'].as_string(),
                    'amplitude': i['amplitude'],
                })

            json_data['n_connections'] = len(self.connections)
        else:
            json_data['connections'] = []

            for i in self.connections:
                json_data['connections'].append(
                    self.__string +
                    '-> ' +
                    i['state'].as_string() +
                    ' (' + to_Hz(i['amplitude']) + ')'
                )

        return json_data

    def get_id(self):
        return self.__id

    def info(self, mode=None):
        if mode == '-v':
            json_data = {'State_' + str(self.__id): self.json_data(mode)}
        else:
            json_data = {self.__string: self.json_data(mode)}

        json_formatted_str = json.dumps(json_data, indent=4, ensure_ascii=False)

        colorful_json = highlight(json_formatted_str, lexers.JsonLexer(), formatters.TerminalFormatter())

        print(colorful_json)
