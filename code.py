from collections import deque

com = int(input())
n_pair = int(input())

graph = [[] for _ in range(com+1)]
visited = [False] * (com + 1)

for _ in range(n_pair):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def bfs_finder(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur_node = queue.popleft()

        for i in graph[cur_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs_finder(1)

result = 0
for i in range(2, com+1):
    if visited[i]: 
        result += 1
    
print(result)
