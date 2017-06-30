from reader.Reader import Reader


def calc_gc(dna):
    return ((dna.count('G') + dna.count('C'))) / (len(dna))


def find_max_gc(dna_list):
    max = 0
    max_name = None
    for d in dna_list:
        dna = calc_gc(d.dna)
        if dna > max:
            max = dna
            max_name = d.name
    return [max_name, max]

reader = Reader()
max_gc = find_max_gc(reader.read_dna('gc','rosalind_gc'))
with open("solution", 'w') as f:
    f.write("{}\n{}".format(max_gc[0], max_gc[1]))
