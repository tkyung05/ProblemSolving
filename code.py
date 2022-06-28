import sys
n = int(sys.stdin.readline())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline())
data.sort(reverse=True)

sub = 0
for i in range(2, n, 3):
    sub += data[i]

print(sum(data) - sub)