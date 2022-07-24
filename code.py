import sys
input = sys.stdin.readline

n = int(input())

leng = len(str(n))
nine_str = '9'
zero_str = '0'

if leng == 1:
    print(n)
    exit(0)
 
result = (n - int((leng - 1) * nine_str)) * leng + 9

for i in range(1, leng - 1):
    result += int(nine_str + (zero_str * i)) * (i + 1)

print(result)