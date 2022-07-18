from collections import deque

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if graph[ny][nx] == '#' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx))

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(T):
    h, w = map(int, input().split())
    
    visited = [[0] * w for _ in range(h) ]
    graph = []
    for _ in range(h):
        graph.append(list(map(str, input().strip('\n'))))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#' and visited[i][j] == 0:
                bfs(i, j)
                result += 1
    
    print(result)
