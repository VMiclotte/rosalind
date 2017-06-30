from reader.Reader import Reader

def transcribe(s):
    with open("solution", 'a') as f:
        f.write(s.replace("T","U"))


reader = Reader()
with open("solution", 'w'):
    pass

transcribe(reader.read('rna','rosalind_rna'))