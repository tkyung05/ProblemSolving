import sys
from collections import deque
input = sys.stdin.readline

result = 0

def bfs(n):
    global result
    q = deque([(n)])
    graph[n] = 1

    while q:
        x = q.popleft()

        if x == k:
            result += 1

        for nx in (x*2, x+1, x-1):
            if nx < 0 or nx > 100000:
                continue
    
            if graph[nx] == 0 or graph[nx] == graph[x] + 1:
                graph[nx] = graph[x] + 1
                q.append(nx)


n, k = map(int, input().split())
graph = [0] * 100001

bfs(n)

print(graph[k] - 1)
print(result)