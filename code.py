import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * (n + 1)

if n < 3:
    print(dp[n])
    exit(0)

dp[3] = 2

for i in range(4, n + 1):
    for j in range(1, i - 1):
        dp[i] += dp[j]

print(dp[n])

