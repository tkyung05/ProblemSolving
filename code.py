import sys
input = sys.stdin.readline

n = int(input())

dp = [0]
for _ in range(n): dp.append(list(map(int, input().split())))

if n == 1:
    print(dp[1][0])
    exit(0)

dp[2][0], dp[2][1] = dp[2][0] + dp[1][0], dp[2][1] + dp[1][0]

for i in range(3, n + 1):
    for j in range(i):
        if j == 0:
            dp[i][0] += dp[i - 1][0]
        elif j == i - 1:
            dp[i][j] += dp[i - 1][j - 1]

        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[-1]))