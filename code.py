import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, -1]
dx = [0, -1, -1]

for i in range(n):
    for j in range(m):
        candy_hold = [0] * 3

        for k in range(3):
            ny, nx = i + dy[k], j + dx[k]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            candy_hold[k] = dp[ny][nx]
            
        dp[i][j] += max(candy_hold)

print(dp[n-1][m-1])