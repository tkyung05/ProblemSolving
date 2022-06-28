import sys
n, m = map(int, sys.stdin.readline().split())
bundle = [0] * m
indiv = [0] * m
for i in range(m):
    bun, ind = map(int, sys.stdin.readline().split())
    bundle[i] = bun
    indiv[i] = ind
bundle.sort()
indiv.sort()

result = [0] * 3
remain = n % 6
share = n // 6

result[0] = bundle[0] * share + indiv[0] * remain
result[1] = bundle[0] * share
if remain > 0:
    result[1] = bundle[0] * (share + 1)
result[2] = indiv[0] * n

print(min(result))