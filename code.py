import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e, k, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append((n2, 1))

def dijkstar(start):
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

dijkstar(start)

bug = True
for i in range(1, v + 1):
    if distance[i] == k:
        print(i)
        bug = False

if bug:
    print(-1)
