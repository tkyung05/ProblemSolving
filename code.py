import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque([(n)])
    graph[n] = 1
    move[n] = -1

    while q:
        x = q.popleft()

        if x == k:
            return graph[x] - 1

        for nx in (x*2, x+1, x-1):
            if nx < 0 or nx > 100000:
                continue
    
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                move[nx] = x
                q.append(nx)


n, k = map(int, input().split())
graph = [0] * 100001
move = [0] * 100001

print(bfs(n))

move_data = []
while True:
    if k == -1:
        break
    move_data.append(k)
    k = move[k]

for i in reversed(move_data):
    print(i, end=' ')

