import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node, count):
    global check

    if count == 5:
        check = True
        return
    
    visited[node] = True
    
    for i in graph[node]:
        if not visited[i]:
            dfs(i, count + 1)
            visited[i] = False


n, e = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

check = False
visited = [False] * n

for i in range(n):
    if check:
        break
    dfs(i, 1)
    visited[i] = False

if check:
    print(1)
else:
    print(0)
