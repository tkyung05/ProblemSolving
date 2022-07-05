from collections import deque
import sys

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
e = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for i in range(e):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [0] * (n + 1)

def bfs():
    queue = deque([start])

    while queue:
        v = queue.popleft()
        
        if v == end:
            return print(visited[v])

        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
    
    return print(-1)

bfs()