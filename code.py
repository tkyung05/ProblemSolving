import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())

input_graph = []
for _ in range(h):
    input_graph.append(list(map(int, input().split())))


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def ice_berg_search(graph):
    temp_graph = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0:
                count = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if graph[ny][nx] == 0:
                        count += 1
                cur_ice = graph[i][j] - count
                if cur_ice < 0:
                    cur_ice = 0
                
                temp_graph[i][j] = cur_ice

    return temp_graph

def bfs(y, x, graph, visited):
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if graph[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
    return visited


check_graph = ice_berg_search(input_graph)
result = 1

while True:
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if check_graph[i][j] != 0 and not visited[i][j]:
                visited = bfs(i, j, check_graph, visited)
                count += 1
    
    if count > 1:
        print(result)
        break
    elif count == 0:
        print(0)
        break
    else:
        check_graph = ice_berg_search(check_graph)
        result += 1 
    