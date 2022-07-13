import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

temp = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            temp.append((graph[i][j], 0, i, j))

temp.sort()
queue = deque(temp)

time, dist_y, dist_x = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while queue:
        virus_num, sec, y, x = queue.popleft()

        if sec == time:
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = virus_num
                queue.append((virus_num, sec + 1, ny, nx)) 
bfs()
print(graph[dist_y - 1][dist_x - 1])

