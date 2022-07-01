from collections import deque

n = int(input())

data = []
def bfs_finder(x, y):
    if graph[x][y] == 0 or graph[x][y] == 2:
        return 0
    
    count = 1

    queue_data = deque()
    queue_data.append((x, y))
    graph[x][y] = 2
    
    while queue_data:
        x, y = queue_data.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]        

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 2
                queue_data.append((nx, ny))

    return count
                    


graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    for j in range(n):
        num = bfs_finder(i, j)
        if num != 0:
            data.append(num)

data.sort()
print(len(data))

for i in data:
    print(i)