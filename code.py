import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    n1, n2, dis = map(int, input().split())
    graph[n1].append((n2, dis))

distance = [INF] * (v + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dis, node = heapq.heappop(q)

        if distance[node] < dis:
            continue
        for i in graph[node]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INF')