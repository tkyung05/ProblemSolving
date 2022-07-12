import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0
            break

for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1 

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []

for i in range(1, v + 1):
    count = 0
    for j in range(1, v + 1):
        count += graph[i][j]
    result.append((count, i))

result.sort()

print(result[0][1])




    