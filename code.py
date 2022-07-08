from collections import deque

f, start, goal, u, d = map(int, input().split()) 

graph = [0] * (f + 1)

def bfs():
    queue = deque([start])
    graph[start] = 1

    while queue:
        cur_pos = queue.popleft()

        if cur_pos == goal:
            return graph[cur_pos] - 1

        for new_pos in (cur_pos+u, cur_pos+(d*-1)):
            if new_pos < 1 or new_pos > f:
                continue
            if graph[new_pos] == 0:
                graph[new_pos] = graph[cur_pos] + 1
                queue.append(new_pos)
    return 'use the stairs'

print(bfs())