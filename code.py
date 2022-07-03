from collections import deque

v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]

dfs_visited = [False] * (v + 1)
bfs_visited = [False] * (v + 1)

for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, v + 1):
    graph[i].sort()


def bfs(start):
    queue = deque()
    queue.append(start)
    bfs_visited[start] = True

    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=' ')

        for i in graph[cur_v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

def dfs(start):
    dfs_visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(i)


dfs(start)
print()
bfs(start)