import sys
input = sys.stdin.readline

n = int(input())
price_data = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1): dp[i] = price_data[i]

if n == 1:
    print(dp[1])
    exit(0)

dp[2] = min(dp[1] * 2, dp[2])
price_data[2] = dp[2]

for i in range(3, n + 1):
    for j in range(1, i // 2 + 1):
        dp[i] = min(dp[i], dp[i - j] + price_data[j])
    price_data[i] = dp[i]

print(dp[n])