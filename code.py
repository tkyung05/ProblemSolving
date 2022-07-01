import sys
sys.setrecursionlimit(10**4)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_finder(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if cab_graph[x][y] == 1:
        cab_graph[x][y] = 0 # 방문 처리
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_finder(nx, ny)
        return True

    return False
        

for _ in range(T):
    w, h, k = map(int, input().split())
    cab_graph = [[0 for _ in range(w)] for _ in range(h)]

    for _ in range(k):
        x, y = map(int, input().split())
        cab_graph[y][x] = 1

    count = 0
    for i in range(h):
        for j in range(w):
            if dfs_finder(i, j):
                count += 1
    
    print(count)
    