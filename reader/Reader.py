import os

from dna.Dna import Dna


class Reader:
    def read(self, package, filename):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__)), package, filename))
        print(__location__)
        with open(__location__) as f:
            read_data = f.read().splitlines()
            return read_data

    def read_dna(self, package, filename):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__)), package, filename))
        print(__location__)
        with open(__location__) as f:
            read_data = f.read().splitlines()
            dna_list  = []
            i = 0
            while i < len(read_data):
                dna_list[i] = Dna(read_data[i][:1],read_data[i+1])
                i += 2
            return dna_list