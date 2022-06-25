import sys
total = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sum_data = [0] * n 

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    sum_data[i] = x * y

if total == sum(sum_data):
    print('Yes')
else:
    print('No')

