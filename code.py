import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

card = [int(input()) for _ in range(n)]

combi = []
result = {}
visited = [False] * n

def dfs(depth):
  if depth == k:
    num = ''
    for i in combi:
      num += str(card[i])
    result[num] = 1
    return

  for i in range(n):
    if not visited[i]:
      visited[i] = True
      combi.append(i)
      
      dfs(depth + 1)
      
      visited[i] = False
      combi.pop()

dfs(0)
print(len(result.values()))