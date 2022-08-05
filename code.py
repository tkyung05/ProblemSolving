import sys
input = sys.stdin.readline

n = int(input())

data = [0]
for _ in range(n): data.append(int(input()))

if n < 3:
    print(sum(data))
    exit(0)

dp = [0] * (n + 1)

dp[1] = data[1]
dp[2] = data[1] + data[2]
dp[3] = max(data[3] + data[1], data[3] + data[2], dp[2])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 1], data[i] + data[i - 1] + dp[i - 3], data[i] + dp[i - 2])

print(dp[-1])