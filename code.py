import sys
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
e = int(input())

distance_graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            distance_graph[i][j] = 0
            break

for _ in range(e):
    n1, n2, dis = map(int, input().split())
    distance_graph[n1][n2] = min(distance_graph[n1][n2], dis)

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            distance_graph[i][j] = min(distance_graph[i][j], distance_graph[i][k] + distance_graph[k][j])

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if distance_graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(distance_graph[i][j], end=' ')
    print()