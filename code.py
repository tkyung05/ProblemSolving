import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited = [False] * 1000001
count = 0
for a, b, c in data:
    if not visited[a] and not visited[b] and not visited[c]:
        count += 1
    visited[a] = True
    visited[b] = True
    visited[c] = True

print(count)