from lib.Assert import Assert
import re

wc = {'1<->0': 0}
# wc = {'0<->1': 1, '0<->1': 2}

wc_parsed = {}

# wc_bin = [0] * self.n_levels

for k in wc.keys():
    levels = re.split('<->|-', k)
    Assert(len(levels) == 2, 'len(levels) != 2')

    # print(levels)
    for i in range(len(levels)):
        try:
            levels[i] = int(levels[i])
        except ValueError as e:
            print('Error:', e)

    levels.sort()

    Assert(levels[0] != levels[1], 'levels[0] == levels[1]')
    # print(levels)

    key = str(levels[0]) + '<->' + str(levels[1])

    Assert(key not in wc_parsed.keys(), 'duplicated keys')
    Assert(wc[k] > 0, 'wc[k] <= 0')

    wc_parsed[key] = wc[k]

    print(wc_parsed)
