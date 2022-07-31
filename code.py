import sys
input = sys.stdin.readline

n = int(input())

limit = 1000
dp = [0] * (limit + 1)

dp[1], dp[2] = 1, 2

for i in range(3, limit + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

