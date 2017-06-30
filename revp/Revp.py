from reader.Reader import Reader


def reverse_palindrome(s,start,length):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    my_string = s[start:start+length]
    reverse = my_string[::-1]
    for i in range(len(my_string)):
        if complements[str(my_string[i])] != reverse[i]:
            return
    with open("solution", 'a') as f:
        f.write(str(start+1) + ' ' + str(length) + "\n")





def all_reverse_palindromes(s):
    string_length = len(s)
    print(s)
    for length in [4,6,8,10,12]:
        i=0
        while i < string_length-length+1:
            reverse_palindrome(s,i,length)
            i+=1
    return

reader = Reader()
dna_list = reader.read_dna('revp','rosalind_revp')
dna = dna_list[0].get_dna()
with open("solution", 'w'):
    pass
all_reverse_palindromes(dna)
