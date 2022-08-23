from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = 0
virus_pos = []
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      virus_pos.append((i, j))

def bfs():
  global result

  visited = [[0] * M for _ in range(N)]

  q = deque([])
  for y, x in virus_pos:
    visited[y][x] = 2
    q.append((y, x))

  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        visited[i][j] = 1
  
  while q:
    y, x = q.popleft()
    
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if ny < 0 or ny >= N or nx < 0 or nx >= M:
        continue

      if visited[ny][nx] == 0:
        visited[ny][nx] = 2
        q.append((ny, nx))

  total = 0
  for i in range(N):
    for j in range(M):
      if visited[i][j] == 0:
        total += 1

  result = max(result, total)


def dfs(depth):
  if depth == 3:
    bfs()
    return
  
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(depth + 1)
        graph[i][j] = 0

dfs(0)
print(result)
