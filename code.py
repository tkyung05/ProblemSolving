import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
result = int(-1e9)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(depth, total, py, px):
    global result

    if depth == k:
        result = max(result, total)
        return

    for i in range(py, n):
        for j in range(px if i == py else 0, m):

            if not visited[i][j]:    
                visit_memo = []
                visited[i][j] = True

                for d in range(4):
                    ny, nx = i + dy[d], j + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if not visited[ny][nx]: 
                        visited[ny][nx] = True
                        visit_memo.append((ny, nx))
                
                dfs(depth + 1, total + graph[i][j], i, j)

                visited[i][j] = False
                for y, x in visit_memo:
                    visited[y][x] = False

dfs(0, 0, 0, 0)
print(result)
