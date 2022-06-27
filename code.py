import sys
n = int(sys.stdin.readline())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline())
data.sort(reverse=True)

result = []
for i in range(n):
    result.append(data[i] * (i + 1))

print(max(result))

