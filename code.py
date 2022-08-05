import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 3 for _ in range(100000 + 1)]

dp[1][0], dp[1][1], dp[1][2] = 3, 1, 1
dp[2][0], dp[2][1], dp[2][2] = 7, 2, 2

div_num = 9901

for i in range(3, n + 1):
    dp[i][1] = (dp[i - 1][0] - dp[i - 1][1]) % div_num
    dp[i][2] = (dp[i - 1][0] - dp[i - 1][2]) % div_num

    dp[i][0] = (dp[i - 1][0] + dp[i][1] + dp[i][2]) % div_num

print(dp[n][0])