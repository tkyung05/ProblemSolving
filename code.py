import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(str, input().strip('\n'))) for _ in range(r)]

visit_alpa = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 1

def dfs(y, x, depth):
    global result

    visit_alpa.append(graph[y][x])

    result = max(result, depth)
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        
        if graph[ny][nx] not in visit_alpa:
            dfs(ny, nx, depth + 1)
            visit_alpa.pop()

dfs(0, 0, 1)
print(result)