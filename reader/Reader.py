import os

from dna.Dna import Dna


class Reader:
    def read(self, package, filename):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__)), package, filename))
        with open(__location__) as f:
            read_data = f.read().replace('\n','')
            return read_data

    def read_lines(self, package, filename):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__)), package, filename))
        with open(__location__) as f:
            read_data = f.readlines()
            i = 0
            while i < len(read_data):
                read_data[i] = read_data[i].replace('\n', '')
                i += 1
            return read_data

    def read_dna(self, package, filename):
        read_data = self.read(package, filename)
        list_data = read_data.split(">")
        dna_list = []
        for s in list_data:
            if s: #only adds non-empty strings
                dna_list.append(Dna(s[13:], s[:13])) #first 12characters are Rosalind_WXYZ
        return dna_list
