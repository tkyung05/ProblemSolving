import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

visited = [False] * n
stack = []

max_total = -1e9


def dfs(depth):
    global max_total

    if depth == n:
        result = 0
        for i in range(1, n):
            result += abs(stack[i - 1] - stack[i])
        max_total = max(result, max_total)
        return
        
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(sequence[i])

            dfs(depth + 1)
            
            visited[i] = False
            stack.pop()
    
dfs(0)

print(max_total)