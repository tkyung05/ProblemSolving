from math import gcd
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = abs(s - data[0])

for i in range(1, n):
    result = gcd(abs(s - data[i]), result)

print(result)
