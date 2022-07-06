from collections import deque
import sys

w, h = map(int, sys.stdin.readline().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, sys.stdin.readline().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


visited = [[0] * w for _ in range(h)]
tomato_node = deque()

zero_check = False

for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            tomato_node.append((i, j))
            visited[i][j] = 1

        elif graph[i][j] == -1:
            visited[i][j] = -1

def bfs():
    while tomato_node:
        y, x = tomato_node.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                tomato_node.append((ny, nx))
bfs()

result = -10
for i in range(h):
    for j in range(w):
        if visited[i][j] == 0:
            result = 0
            break
        elif visited[i][j] > result:
            result = visited[i][j]
    
    if result == 0:
        break

print(result - 1)