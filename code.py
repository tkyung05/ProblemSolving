from collections import deque

n = int(input())

max_num = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(n):
        if max_num < graph[i][j]:
            max_num = graph[i][j]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, value, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > value and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


result = 0
for i in range(max_num):
    visited = [[False] * n for _ in range(n)]
    
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                count += 1

    if result < count:
        result = count

print(result)
    
    