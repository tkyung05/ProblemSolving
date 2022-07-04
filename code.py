import sys
sys.setrecursionlimit(10 ** 5)

v, e, start = map(int, input().split())

visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, v + 1):
    graph[i].sort()

data = []
def dfs(start):
    visited[start] = True
    data.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(start)

result = [0] * (v + 1)
for i in range(len(data)):
    result[data[i]] = i + 1

for i in range(1, len(result)):
    print(result[i])


