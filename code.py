LIMIT = 2001
DIV_NUM = 1234567


def solution(n):
    dp = [0] * LIMIT
    dp[1], dp[2] = 1, 2

    for i in range(3, LIMIT):
        dp[i] = (dp[i - 1] + dp[i - 2]) % DIV_NUM

    return dp[n]
