from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    q.appendleft((y, x))
    visited[y][x][0] = 1 # 방문 체크 카운트
    visited[y][x][1] = 0 # 상태 값 : 다람쥐 = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if graph[ny][nx] == 'D' and visited[y][x][1] == 0:
                return visited[y][x][0]
            
            # 자신이 물인 경우
            if graph[ny][nx] == '.' and visited[y][x][1] == 1 and visited[ny][nx][0] >= 0:
                visited[ny][nx][0] = -1
                visited[ny][nx][1] = 1
                q.append((ny, nx))
            
            # 자신이 다람쥐인 경우
            if graph[ny][nx] == '.' and visited[y][x][1] == 0 and visited[y][x][0] > 0 and visited[ny][nx][0] == 0:
                visited[ny][nx][0] = visited[y][x][0] + 1
                visited[ny][nx][1] = 0
                q.append((ny, nx))
     
    return 'KAKTUS'
                

h, w = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(str, input().strip('\n'))))

visited = [[[0] * 2 for _ in range(w)] for _ in range(h)]

s_y, s_x = 0, 0
q = deque()

for i in range(h):
    for j in range(w):
        if graph[i][j] == '*':
            q.append((i, j))
            visited[i][j][0] = -1 # 방문 체크
            visited[i][j][1] = 1 # 상태 값 : 물 = 1, 다람쥐 = 0 
        elif graph[i][j] == 'S':
            graph[i][j] = '.'
            s_y, s_x = i, j

print(bfs(s_y, s_x))