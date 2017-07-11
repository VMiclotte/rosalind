from reader.Reader import Reader
import itertools

def permute(list1, low=0):
    list1 = list1[:] #copy of list1 so there's not the same list being added over and over again in permutations function
    if low + 1 >= len(list1):
        yield list1
    else:
        for p in permute(list1, low + 1):
            yield p
        for i in range(low + 1, len(list1)):
            list1[low], list1[i] = list1[i], list1[low]
            for p in permute(list1, low + 1):
                yield p
            list1[low], list1[i] = list1[i], list1[low]


def list_to_string(list1):
    s = ''
    for i in range(len(list1) - 1):
        s += str(list1[i]) + ' '
    s += str(list1[len(list1) - 1])
    return s


def permutations(n):
    list1 = [x + 1 for x in range(n)]
    amt = 1
    for i in range(n):
        amt *= (i + 1)
    return [p for p in permute(list1)]

def sign(n):
    signs = []
    perms = permutations(n)
    binary = [list(seq) for seq in itertools.product("01", repeat=n)]
    for p in perms:
        for bin in binary:
            p1 = p[:]
            for i in range(len(bin)):
                if bin[i]=='0':
                    p1[i] = -1*p1[i]
            signs.append(p1)
    return signs


reader = Reader()
with open("solution", 'w'):
    pass
n = int(reader.read("sign","rosalind_sign"))
signs = sign(n)
with open("solution", 'a') as f:
    f.write(str(len(signs)) + "\n")
    for p in signs:
        f.write(list_to_string(p) + "\n")




