import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 5

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

visited = [False] * 10001
result = []

def dfs(count):
    if count == m:
        print(' '.join(list(map(str, result))))
        return 
    
    for i in data:
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(count + 1)
            
            visited[i] = False
            result.pop()


dfs(0)