import itertools


def list_to_string(list1):
    s = ''
    for i in range(len(list1) - 1):
        s += str(list1[i]) + ' '
    s += str(list1[len(list1) - 1])
    return s

n = 4
for bin in [list(seq) for seq in itertools.product("01", repeat=n)]:
    print(list_to_string(bin))