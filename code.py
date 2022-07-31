import sys
input = sys.stdin.readline

T = int(input())

limit = 11

for _ in range(T):
    n = int(input())

    dp = [0] * (limit + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    print(dp[n])
    