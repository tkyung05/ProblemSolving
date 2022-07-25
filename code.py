import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 5

n, m = map(int, input().split())

result = []

def dfs(count):
    if count == m:
        print(' '.join(list(map(str, result))))
        return 
    
    for i in range(1, n + 1):            
        result.append(i)
        dfs(count + 1)
        result.pop()

dfs(0)