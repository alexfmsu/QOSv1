import numpy as np
import itertools

import functools as ft


def flattenNestedList(nestedList):
    ''' Converts a nested list to a flat list '''
    flatList = []
    # Iterate over all the elements in given list
    for elem in nestedList:
        # Check if type of element is list
        if isinstance(elem, list):
            # Extend the flat list by adding contents of this element (list)
            flatList.extend(flattenNestedList(elem))
        else:
            # Append the elemengt to the list
            flatList.append(elem)

    return flatList

a = [[1, [2]], 3]
a = np.array(a)
# result = ft.reduce(lambda x, y: x + y, a)
# chain = itertools.chain(*a)
# print(list(chain))
# b = np.hstack(a)
# b = np.concatenate(a, axis=2)
# print(extend(a))
# print(str(a[:]))
print(flattenNestedList(a))
exit(0)


a = np.array([1, 2, 3, 4, 5, 6, 7])
# indices = [0, 2]
# s = a[indices].sum()
# print(s)

indices = [[0, 2], [3, 4]]

# s = [x for a[indices[:]]

# print(a)

# subset = a[1:3]
# np.insert(1, subset)
# a[1:3]

# print(a)
y = []
# x = [[1, 2], [3, 4], [5, 6]]
for i in indices:
    print(a[i[0]:i[1]])
    y += list(a[i[0]:i[1]])
# y = a[indices[1]]
# y = a[indices[0]] + a[indices[1]]
# y = []
# for i in indices:
#     y += list(a[i])
# y = sum(a[indices[i]] for i in range(len(indices)), [])
# y = list(itertools.chain(l1, l2, l3))
# y = x[0] + x[1]
# y = [add(i) for i in x]

print(y)
