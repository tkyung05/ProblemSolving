from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    q.appendleft((y, x))
    visited[y][x][0] = 1

    while q:
        y, x = q.popleft()

        if (y == (h - 1) or x == (w - 1) or y == 0 or x == 0) and graph[y][x] == '.' and visited[y][x][1] == 0:
            return visited[y][x][0]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            
            # 지훈이인 경우
            if visited[y][x][1] == 0 and graph[ny][nx] == '.' and visited[ny][nx][0] == 0:
                visited[ny][nx][0] = visited[y][x][0] + 1
                q.append((ny, nx))

            # 불인 경우
            elif visited[y][x][1] == 1 and graph[ny][nx] == '.' and visited[ny][nx][0] >= 0:
                visited[ny][nx][1] = 1
                visited[ny][nx][0] = -1
                q.append((ny, nx))
    
    return 'IMPOSSIBLE'
                


h, w = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(str, input().strip('\n'))))

visited = [[[0] * 2 for _ in range(w)] for _ in range(h)]

q = deque()
j_y, j_x = 0, 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'F':
            q.append((i, j))
            visited[i][j][0] = -1 # 방문 처리
            visited[i][j][1] = 1 # 1 = 불, 0 = 지훈
        elif graph[i][j] == 'J':
            j_y, j_x = i, j
            graph[i][j] = '.'

print(bfs(j_y, j_x))