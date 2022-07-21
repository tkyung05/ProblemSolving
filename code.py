import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque([(n)])
    graph[n] = 1

    while q:
        x = q.popleft()

        if x == k:
            return graph[x] - 1

        tel_x = x * 2
        if tel_x <= 100000:
            graph[tel_x] = graph[x]
            q.append(tel_x)

        for nx in (x-1, x+1):
            if nx < 0 or nx > 100000:
                continue
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)
        

n, k = map(int, input().split())
graph = [0] * 100001

print(bfs(n))


