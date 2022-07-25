import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1) # (1 ~ n)각 수의 최소 연산 횟수를 저장할 메모장

# 상향식 이유 => (1부터 n까지, n부터 1까지) 연산 횟수는 동일하기 때문. 
for i in range(2, n + 1):
    # i에 도달 하기 위한 최소 연산 횟수를 구할 수 있음.
    # 점화식 : min(dp[i - 1] + 1, dp[i // 2] + 1, dp[i // 3] + 1)
    
    dp[i] = dp[i - 1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
