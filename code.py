from collections import deque

n, k = map(int, input().split())
max_num = 100001

pos = [0] * max_num

def bfs(x):
    queue = deque([x])
    
    while queue:
        x = queue.popleft()
        if x == k:
            return pos[x]

        for nx in (x - 1, x + 1, x * 2):
            if nx < 0 or nx >= max_num:
                continue
            if not pos[nx]:
                pos[nx] = pos[x] + 1
                queue.append(nx)

print(bfs(n))