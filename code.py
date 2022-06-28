from random import randrange
import sys
n = int(sys.stdin.readline())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline())
data.sort()

result = [0] * n
for i in range(n):
    result[i] = abs(data[i] - (i+1))
print(sum(result))