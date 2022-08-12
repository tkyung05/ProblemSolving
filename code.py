from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        y, x, h = q.popleft()

        if y == N - 1 and x == M - 1:
            f, s = int(1e9), int(1e9)

            if visited[y][x][0] != 0 and visited[y][x][0] - 1 <= T:
                f = visited[y][x][0] - 1

            if visited[y][x][1] != 0 and visited[y][x][1] - 1 <= T:
                s = visited[y][x][1] - 1
            
            result = min(f, s)
            if result == int(1e9):
                return 'Fail'
            
            return result

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            
            if h == 1 and visited[ny][nx][1] == 0:
                visited[ny][nx][1] = visited[y][x][1] + 1
                q.append((ny, nx, 1))
            
            if h == 0 and graph[ny][nx] == 0 and visited[ny][nx][0] == 0:
                visited[ny][nx][0] = visited[y][x][0] + 1
                q.append((ny, nx, 0))

            if h == 0 and graph[ny][nx] == 2 and visited[ny][nx][0] == 0:
                visited[ny][nx][1] = visited[y][x][0] + 1
                q.append((ny, nx, 1))
            
    return 'Fail'


print(bfs())
