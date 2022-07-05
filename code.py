import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())
graph = []
for i in range(h):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx, ny))
    
result = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            bfs(i, j)
            result += 1

print(result)