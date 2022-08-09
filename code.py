import sys
input = sys.stdin.readline

n = int(input())

result = []
visited = [False] * n

def dfs(depth):
    if depth == n:
        print(' '.join(list(map(str, result))))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            
            dfs(depth + 1)
            
            visited[i] = False
            result.pop()
    
dfs(0)