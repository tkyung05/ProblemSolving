import sys
n, m = map(int, sys.stdin.readline().split())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline())
data.sort()

left = 0
right = 1
most_min = 2000000000

while left < n and  right < n:
    sub = data[right] - data[left]

    if most_min > sub and m <= sub:
        most_min = sub
        if most_min == m:
            break
        left += 1
    
    elif sub > m:
        left += 1
    elif sub < m:
        right += 1

print(most_min)