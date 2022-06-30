import sys
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline())))

def bfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x, y] == 0:
        graph[x, y] = 1 # 방문 처리

        # 재귀로 주변 상하좌우 모두 호출하여 방문처리
        bfs(x - 1, y) 
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs(x, y + 1)

        # 처음 0 발견한 한번만 True 리턴
        return True
    # 1이라면 그냥 False 리턴 
    return False

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)