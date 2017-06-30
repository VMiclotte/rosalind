from reader.Reader import Reader

def fib(n,k):
    now = 1
    last_month = 1
    i = 2
    while i < n:
        temp = now
        now = now + last_month*k
        last_month = temp
        i += 1
    return now

reader = Reader()
file = reader.read('fib','rosalind_fib').split()
with open("solution", 'w') as f:
    f.write(str(fib(int(file[0]),int(file[1]))))