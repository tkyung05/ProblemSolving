from collections import deque

n = int(input())
cur_x, cur_y, dis_x, dis_y = map(int, input().split())

graph = [[0] * n for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
    queue = deque([(cur_x, cur_y)])
    graph[cur_x][cur_y] = 1
    
    while queue:
        x, y = queue.popleft()
        if x == dis_x and y == dis_y:
            return graph[x][y]  

        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return 0
            
print(bfs() - 1)