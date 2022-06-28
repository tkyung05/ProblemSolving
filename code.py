import sys
n = int(sys.stdin.readline())

tip = [0] * n
for i in range(n):
    tip[i] = int(sys.stdin.readline())
tip.sort(reverse=True)

result = []
for i in range(n):
    v = tip[i] - i
    if v > 0:
        result.append(v)
    else:
        continue

print(sum(result))