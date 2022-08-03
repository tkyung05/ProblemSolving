import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [1] * n
lis = data.copy()

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            before = dp[i]
            dp[i] = max(dp[i], dp[j] + 1)

            if before != dp[i]:
                lis[i] = j

top_index = dp.index(max(dp))

print(dp[top_index])

result_lis = []
for _ in range(dp[top_index]):
    result_lis.append(data[top_index])
    top_index = lis[top_index]
result_lis.reverse()

print(' '.join(list(map(str,result_lis))))
