import sys
from collections import deque
sys.setrecursionlimit(10**4)


def bfs_finder(x, y):
    if graph[x][y] == 0:
        return 0
    
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                count += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0
    
    return count


h, w = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))

result = []
for i in range(h):
    for j in range(w):
        num = bfs_finder(i, j)
        if num != 0:
            result.append(num)
            
if len(result) == 0:
    print(0)
    print(0)
else:
    result.sort(reverse=True)
    print(len(result))
    print(result[0])    
