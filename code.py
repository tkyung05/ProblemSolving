import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, n): data[i] += data[i - 1]

for i in range(m):
    start, end = map(int, input().split())
    
    start -= 1
    end -= 1

    if start == 0:
        print(data[end])
    else:
        print(data[end] - data[start - 1])
