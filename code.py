import sys
input = sys.stdin.readline

n = int(input())

data = [0] * n
for i in range(n):
    data[i] = int(input())
data.reverse()


result = 0
for i in range(n - 1):
    cur, pront = data[i], data[i + 1]

    if cur <= pront:
        min_gap = pront - cur + 1
        result += min_gap
        data[i + 1] = pront - min_gap

print(result)