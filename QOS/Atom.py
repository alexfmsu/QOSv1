# =================================================== DESCRIPTION =====================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== DESCRIPTION =====================================================


# =================================================== EXAMPLES ========================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== EXAMPLES ========================================================


# =====================================================================================================================
# QOS
from QOS.ElectronShell import ElectronShell
# ---------------------------------------------------------------------------------------------------------------------
# utils
from utils.ParseJumps import *
# =====================================================================================================================


class Atom:
    __slots__ = ['__id', 'wa', 'g', '__n_levels', 'pos', 'electron_shell', '__in_use', 'jumps', 'lvl']

    __ID = 0

    def json_data(self, mode):
        json_data = {}

        if mode == '-v':
            json_data['id'] = self.__id
            json_data['in_use'] = self.__in_use

        json_data['n_levels'] = self.__n_levels
        json_data['g'] = {}

        for k, v in self.g.items():
            json_data['g'][k] = v['value']

        return json_data

    def __init__(self, wa, g, id=None, n_levels=None, electron_shell=None, pos=None):
        if id is None:
            self.__id = Atom.__ID
            Atom.__ID += 1

        self.unlock()
        self.pos = pos
        self.lvl = 0
        if electron_shell is not None:
            self.electron_shell = ElectronShell(electron_shell)

        self.wa = parse_jumps(wa)
        self.g = parse_jumps(g)

        # print(self.wa)
        # exit(0)
        self.__n_levels = max([wa['levels'][1] for wa in self.wa.values()]) + 1

        Assert(set(self.wa.keys()) == set(self.g.keys()), 'set(self.wa.keys()) != set(self.g.keys())')

        self.jumps = self.g.keys()

    def n_levels(self):
        return self.__n_levels

    def lock(self):
        self.__in_use = True

    def unlock(self):
        self.__in_use = False

    def in_use(self):
        return self.__in_use
    # -----------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------- WC_INFO ----------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    def wa_info(self, prefix=None):
        print('wa: ', color='yellow', attrs=['bold'], prefix=prefix)

        for i in self.wa:
            print(i['notation'], ':\t', to_Hz(i['value']), sep='', prefix=prefix)
            # print(k, ':\n\t', to_Hz(self.wc_parsed[k]), sep='')

        # if isinstance(self.wc, dict):
        #     print()

        #     for k in self.wc.keys():
        #         print(k, ':\n\t', to_Hz(self.wc[k]), sep='')
        # else:
        #     print(to_Hz(self.wc), sep='')

        print()
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------- G_INFO -----------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    def g_info(self, prefix=None):
        print('g: ', color='yellow', attrs=['bold'], prefix=prefix)

        for i in self.g:
            print(i['notation'], ':\t', to_Hz(i['value']), sep='', prefix=prefix)
            # print(k, ':\n\t', to_Hz(self.wc_parsed[k]), sep='')

        # if isinstance(self.wc, dict):
        #     print()

        #     for k in self.wc.keys():
        #         print(k, ':\n\t', to_Hz(self.wc[k]), sep='')
        # else:
        #     print(to_Hz(self.wc), sep='')

        print()
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def info(self, prefix='', mode=None):
        json_data = {'Atom_' + str(self.get_id()): self.json_data(mode)}

        json_formatted_str = json.dumps(json_data, indent=4)

        colorful_json = highlight(json_formatted_str, lexers.JsonLexer(), formatters.TerminalFormatter())

        print(colorful_json)

        # print('id: ', self.id, sep='', prefix=prefix)
        # print('n_levels: ', self.n_levels, sep='', prefix=prefix)

        # self.wa_info(prefix=prefix)
        # self.g_info(prefix=prefix)

        # print('electron_shell: ', sep='', end='', prefix=prefix)
        # self.electron_shell.info()
        # print('spins:', self.spins)
