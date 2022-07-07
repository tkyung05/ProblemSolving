from collections import deque

w, h = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * w for _ in range(h)]

def bfs(y, x, team):
    queue = deque([(y, x)])
    visited[y][x] = True
    count = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if team == graph[ny][nx] and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
                count += 1
    return count ** 2

W_result = 0
B_result = 0

for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                W_result += bfs(i, j, graph[i][j])
            elif graph[i][j] == 'B':
                B_result += bfs(i, j, graph[i][j])

print(W_result, B_result)

