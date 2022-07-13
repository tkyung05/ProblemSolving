import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1) 

for _ in range(e):
    n1, n2, dis = map(int, input().split())
    graph[n1].append((n2, dis))

start_v, target_v = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for i in graph[node]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_v)
print(distance[target_v])