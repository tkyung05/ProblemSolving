import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = []
    for _ in range(2): dp.append([0] + list(map(int, input().split())))

    if n == 1:
        print(max(dp[0][1], dp[1][1]))
        continue

    dp[0][2] += dp[1][1]
    dp[1][2] += dp[0][1] 

    for i in range(3, n + 1):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2]) 
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][n], dp[1][n]))