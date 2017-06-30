from reader.Reader import Reader


def hamm(p, q):
    i = 0
    dist = 0
    while i < len(p):
        if p[i] != q[i]:
            dist += 1
        i += 1
    return dist


reader = Reader()
lines = reader.read_lines('hamm', 'rosalind_hamm')

with open("solution", 'w') as f:
    f.write(str(hamm(lines[0], lines[1])))
