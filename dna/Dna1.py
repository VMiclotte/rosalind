from dna.Dna import Dna
from reader.Reader import Reader

reader = Reader()
dna = Dna(reader.read('dna', 'rosalind_dna'))
count = dna.count()
with open("solution", 'w'):
    pass
with open("solution", "a") as f:
    f.write("{} {} {} {}".format(count[0],count[1],count[2],count[3]))