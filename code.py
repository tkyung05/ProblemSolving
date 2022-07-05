n, m = map(int, input().split(':'))

def GCD(n, m):
    while True:
        tmp = n % m
        if tmp == 0:
            return m
        n = m
        m = tmp 
        
GCD_num = GCD(max(n, m), min(n, m))

print(f'{n // GCD_num}:{m // GCD_num}')