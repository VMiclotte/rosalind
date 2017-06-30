from reader.Reader import Reader

def complement(s):
    reverse =  s[::-1]
    reverse = reverse.replace("A", "U")
    reverse = reverse.replace("T", "A")
    reverse = reverse.replace("U", "T")
    reverse = reverse.replace("C", "U")
    reverse = reverse.replace("G", "C")
    reverse = reverse.replace("U", "G")
    return reverse
reader = Reader()
with open("solution", 'w') as f:
    f.write(complement(reader.read('revc','rosalind_revc')))
