from collections import deque

h, w = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(input()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[False] * w for _ in range(h)]

all_sheep = 0
all_wolf = 0

def bfs(y, x):
    global all_sheep
    global all_wolf

    sheep = 0
    wolf = 0
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        if graph[y][x] == 'o':
            sheep += 1
        elif graph[y][x] == 'v':
            wolf += 1

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            elif graph[ny][nx] == '.' and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

            elif (graph[ny][nx] == 'o' or graph[ny][nx] == 'v') and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    
    if sheep > wolf:
        wolf = 0
    elif sheep <= wolf:
        sheep = 0

    all_sheep += sheep
    all_wolf += wolf


for i in range(h):
    for j in range(w):
        if (graph[i][j] == 'o' or graph[i][j] == 'v') and not visited[i][j]:
            bfs(i, j)

print(all_sheep, all_wolf)
