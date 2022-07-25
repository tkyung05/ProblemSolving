import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 5

n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(count):
    if count == m:
        print(' '.join(list(map(str, result))))
        return 
    
    for i in range(1, n + 1):
        if not visited[i] and len(result) == 0 or result[-1] < i:
            visited[i] = True
            result.append(i)
            dfs(count + 1)
            result.pop()
            visited[i] = False

dfs(0)