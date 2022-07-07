from collections import deque

h, w = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int, input())))

visited = [[False] * w for _ in range(h)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

for i in range(w):
    if graph[0][i] == 0 and not visited[0][i]:
        bfs(0, i)

trig = False
for i in range(w):
    if graph[h-1][i] == 0 and visited[h-1][i]:
        trig = True
        break

if trig:
    print('YES')
else:
    print('NO')



