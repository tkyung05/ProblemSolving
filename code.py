from collections import deque

n = int(input())
leng = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(leng):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def bfs():
    queue = deque([1])
    visited[1] = 1
    count = 0

    while queue:
        v = queue.popleft()

        if visited[v] == 3:
            return count

        for i in graph[v]:
            if not visited[i]:
                count += 1
                visited[i] = visited[v] + 1
                queue.append(i)
    return count

print(bfs())