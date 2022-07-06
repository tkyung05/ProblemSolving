from collections import deque

a, b = map(int, input().split())

limit = 1000000001
graph = {}

def bfs(a):
    queue = deque([a])
    graph[str(a)] = 1

    while queue:
        n = queue.popleft()
        one_n = int(str(n) + '1')

        if n == b:
            return print(graph[str(n)]) 

        for i in (n*2, one_n):
            if i < 0 or i >= limit:
                continue
            if not str(i) in graph:
                graph[str(i)] = graph[str(n)] + 1
                queue.append(i)

    return print(-1)

bfs(a)