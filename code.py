import sys
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for day in range(n-1, -1, -1):
  time = work[day][0]
  
  if day + time <= n:
    price = work[day][1]  
    dp[day] = max(dp[day + 1], dp[day + time] + price)
  else:
    dp[day] = dp[day + 1]

print(dp[0])