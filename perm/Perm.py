from reader.Reader import Reader


def permute(list1, low=0):
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
    for i in range(len(list1)-1):
        s += str(list1[i]) + ' '
    s += str(list1[len(list1)-1])
    return s

def permutations(n):
    list1 = [x+1 for x in range(n)]
    amt = 1
    for i in range(n):
        amt *= (i+1)
    with open("solution", 'a') as f:
        f.write(str(amt)+"\n")
        for p in permute(list1):
            f.write(list_to_string(p)+"\n")

reader = Reader()
with open("solution", 'w'):
    pass
permutations(int(reader.read("perm","rosalind_perm")))
