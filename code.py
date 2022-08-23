import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

result = {}
max_v = 20 * int(1e5) + 1

def dfs(idx, total):
  if idx == n:
    return
  
  total += card[idx]
  result[total] = 1

  dfs(idx + 1, total)
  dfs(idx + 1, total - card[idx])

dfs(0, 0)

for i in range(1, max_v):
  if i not in result:
    print(i)
    break