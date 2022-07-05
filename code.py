from collections import deque
import sys


T = int(sys.stdin.readline())

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

def bfs(x, y, dis_x, dis_y, n, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        if x == dis_x and y == dis_y:
            return graph[x][y]

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))



for _ in range(T):
    n = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    dis_x, dis_y = map(int, sys.stdin.readline().split())

    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    print(bfs(x, y, dis_x, dis_y, n, visited))
    

    
    