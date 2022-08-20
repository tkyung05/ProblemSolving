import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, n): data[i] += data[i - 1]

result = data[k - 1]
for i in range(n - k): result = max(result, data[k + i] - data[i])

print(result)