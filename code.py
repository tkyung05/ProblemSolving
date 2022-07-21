import sys
from collections import deque
input = sys.stdin.readline
limit = 100000

dx = [1, 2]

def bfs(n):
    q = deque([(n)])
    graph[n] = 1

    while q:
        x = q.popleft()

        if graph[x] - 1 > t:
            return 'ANG'
        if x == g:
            return graph[x] - 1 

        for i in range(2):
            if i == 0:
                btn = x + dx[i]
                if btn >= limit:
                    continue
                
            elif i == 1:
                btn = x * dx[i]
                if btn >= limit:
                    continue
                if btn > 0 and btn < 10:
                    btn -= 1
                elif btn > 0:
                    btn = btn - (10 ** (len(str(btn))-1))

            if graph[btn] == 0:
                graph[btn] = graph[x] + 1
                q.append(btn)

    return 'ANG'
                

    


graph = [0] * limit
n, t, g = map(int, input().split())

print(bfs(n))