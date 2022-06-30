from collections import deque

h, w = map(int, input().split())

def bfs_check(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] != 1:
                continue
            
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    return print(graph[h - 1][w - 1])
        

graph = []
for _ in range(h):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs_check(0, 0)