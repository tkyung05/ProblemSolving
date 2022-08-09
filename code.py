import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
sequence = []

min_cost = int(1e9)

def dfs(depth):
    global min_cost

    if depth == n:
        total_cost = 0
        for i in range(n):
            if i == n - 1:
                start, end = sequence[i], sequence[0]
            else: 
                start, end = sequence[i], sequence[i + 1]

            c = graph[start][end]
            
            if c == 0: return
            else: total_cost += c

        min_cost = min(total_cost, min_cost)
        return
        
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)

            dfs(depth + 1)
            
            visited[i] = False
            sequence.pop()

dfs(0)

print(min_cost)