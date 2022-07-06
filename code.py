from collections import deque
import sys

h, w, k = map(int, sys.stdin.readline().split())

graph = [[0] * w for _ in range(h)]
for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())
    graph[y-1][x-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque([(y, x)])
    graph[y][x] = 2
    count = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if graph[ny][nx] == 1:
                count += 1
                graph[ny][nx] = 2
                queue.append((ny, nx))
    
    return count

result = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            num = bfs(i, j)
            if result < num:
                result = num

print(result)



