import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
sequence = []
teacher = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'S':
            visited[i][j] = True

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def check():
    for y, x in teacher:
        for i in range(4):
            
            for j in range(n):
                if i == 0 or i == 1:
                    ny = dy[i] + (j * dy[i])
                    nx = 0
                elif i == 2 or i == 3:
                    nx = dx[i] + (j * dx[i])
                    ny = 0
                
                cy, cx = y + ny, x + nx
                if cy < 0 or cy >= n or cx < 0 or cx >= n:
                    break

                if graph[cy][cx] == 'O':
                    break
                if graph[cy][cx] == 'S':
                    return False
    return True


def dfs(depth, idx):

    if depth == 3:
        if check():
            print('YES')
            exit(0)
        return
    
    for i in range(idx, n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                graph[i][j] = 'O'

                dfs(depth + 1, i)

                visited[i][j] = False
                graph[i][j] = 'X'

dfs(0, 0)

print('NO')