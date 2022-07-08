from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

item = {}
for _ in range(n+m):
    n1, n2 = map(int, sys.stdin.readline().split())
    item[str(n1)] = n2

graph = [0] * 101
dice = [1, 2, 3, 4, 5, 6]

def bfs():
    queue = deque([1])
    graph[1] = 1
    
    while queue:
        cur_pos = queue.popleft()
        if cur_pos == 100:
            return graph[cur_pos] - 1

        for i in range(6):
            new_pos = cur_pos + dice[i]
            
            if new_pos > 100:
                continue
            
            if str(new_pos) in item and graph[new_pos] == 0:
                if graph[item[str(new_pos)]] == 0:
                    new_pos = item[str(new_pos)]
                    graph[new_pos] = graph[cur_pos] + 1
                    queue.append(new_pos)

            elif graph[new_pos] == 0:
                graph[new_pos] = graph[cur_pos] + 1
                queue.append(new_pos)

print(bfs())