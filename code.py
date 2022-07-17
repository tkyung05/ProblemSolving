import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(n):
    q = deque([n])
    visited[n] = 1

    while q:
        n = q.popleft()

        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n] * -1
                q.append(i)
            else:
                if visited[n] == visited[i]:
                    return False
    return True


for _ in range(T):
    v, e = map(int, input().split())

    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    bug = False

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                bug = True
                break
    
    if bug:
        print('NO')
    else:
        print('YES')

    