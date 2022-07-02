from collections import deque

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for i in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur_node = queue.popleft()
        for i in graph[cur_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
result = 0
for i in range(1, v + 1):
    if not visited[i]:
        bfs(i)
        result += 1
    
print(result)