import sys
n, k = map(int, sys.stdin.readline().split())
data = [0] * n

for i in range(n):
    data[i] = int(sys.stdin.readline())
data.sort(reverse=True)

count = 0

for i in range(n):
    if k == 0:
        break
    if data[i] <= k:
        count += (k // data[i])
        k %= data[i]
         
print(count)
