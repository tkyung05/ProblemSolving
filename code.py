import sys
input = sys.stdin.readline

limit = 100001
div_num = 1000000009

T = int(input())

dp = [[0] * 4 for _ in range(limit)]

dp[1][0], dp[1][1] = 1, 1
dp[2][0], dp[2][2] = 1, 1
dp[3][0], dp[3][1], dp[3][2], dp[3][3] = 3, 1, 1, 1

for i in range(4, limit):
    dp[i][1] = dp[i - 1][0] - dp[i - 1][1]
    dp[i][2] = dp[i - 2][0] - dp[i - 2][2]
    dp[i][3] = dp[i - 3][0] - dp[i - 3][3]
        
    dp[i][0] = (dp[i][1] + dp[i][2] + dp[i][3]) % div_num

for _ in range(T): 
    n = int(input())
    print(dp[n][0])