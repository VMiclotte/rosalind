class Dna:
    name = ""
    dna = ""

    def __init__(self,dna, name=None):
        self.name = name
        self.dna = dna

    def get_dna(self):
        return self.dna

    def get_name(self):
        return self.name

    def count(self):
        a = 0
        c = 0
        g = 0
        t = 0
        for character in self.dna:
            if character == 'A':
                a += 1
            elif character == 'C':
                c += 1
            elif character == 'G':
                g += 1
            elif character == 'T':
                t += 1
        return [a, c, g, t]
