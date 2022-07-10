from collections import deque

h, w = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int, input())))
        
visited = [[[0] * 2 for _ in range(w)] for _ in range(h)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0][1] = 1

    while queue:
        y, x, key = queue.popleft()

        if y == h - 1 and x == w - 1:
            return visited[y][x][key]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            
            if graph[ny][nx] == 1 and key == 1:
                visited[ny][nx][0] = visited[y][x][1] + 1
                queue.append((ny, nx, 0))

            elif graph[ny][nx] == 0 and visited[ny][nx][key] == 0:
                visited[ny][nx][key] = visited[y][x][key] + 1
                queue.append((ny, nx, key))

    return -1
    
print(bfs())
    