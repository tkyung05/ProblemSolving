import sys
n = int(sys.stdin.readline())
leng_data = list(map(int, sys.stdin.readline().split()))
oil_data = list(map(int, sys.stdin.readline().split()))

result = 0
now_oil = oil_data[0]

for i in range(n - 1):
    result += now_oil * leng_data[i] 
    if now_oil > oil_data[i + 1]:
        now_oil = oil_data[i + 1]

print(result)
