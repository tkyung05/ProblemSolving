from collections import deque
import sys

w, h, box = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(box)]
for i in range(box):
    for _ in range(h):
        graph[i].append(list(map(int, sys.stdin.readline().split())))


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[[0] * w for _ in range(h)] for _ in range(box)]
tomato_node = deque()

for b in range(box):
    for i in range(h):
        for j in range(w):
            if graph[b][i][j] == 1:
                tomato_node.append((b, i, j))
                visited[b][i][j] = 1

            elif graph[b][i][j] == -1:
                visited[b][i][j] = -1

def bfs():
    while tomato_node:
        b, y, x = tomato_node.popleft()

        # 앞, 뒤, 좌, 우
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if visited[b][ny][nx] == 0:
                visited[b][ny][nx] = visited[b][y][x] + 1
                tomato_node.append((b, ny, nx))
        # 상, 하
        if (b - 1) >= 0 and visited[b-1][y][x] == 0:
            visited[b - 1][y][x] = visited[b][y][x] + 1
            tomato_node.append((b-1, y, x))

        if (b + 1) < box and visited[b+1][y][x] == 0:
            visited[b + 1][y][x] = visited[b][y][x] + 1
            tomato_node.append((b+1, y, x))


result = -10

def check():
    global result

    for b in range(box):
        for i in range(h):
            for j in range(w):
                if visited[b][i][j] == 0:
                    result = 0
                    return 
                elif visited[b][i][j] > result:
                    result = visited[b][i][j]

bfs()
check()

print(result - 1)
