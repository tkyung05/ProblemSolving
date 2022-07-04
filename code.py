from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def org_bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    org_visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == color and not org_visited[nx][ny]:
                org_visited[nx][ny] = True
                queue.append((nx, ny))


def str_bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    str_visited[x][y] = True
    
    if color == 'R' or color == 'G':
        color, color2 = 'R', 'G'
    else:
        color, color2 = 'B', 'B' 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (graph[nx][ny] == color or graph[nx][ny] == color2) and not str_visited[nx][ny]:
                str_visited[nx][ny] = True
                queue.append((nx, ny))


org_visited = [[False] * n for _ in range(n)]
str_visited = [[False] * n for _ in range(n)]

org_result = 0
str_result = 0

for i in range(n):
    for j in range(n):
        if not org_visited[i][j]:
            org_bfs(i, j, graph[i][j])
            org_result += 1

        if not str_visited[i][j]:
            str_bfs(i, j, graph[i][j]) 
            str_result += 1

print(org_result, str_result)