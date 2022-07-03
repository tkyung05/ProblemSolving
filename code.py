n = int(input())

org_count = 0

def original_fibo(n):
    global org_count

    if n == 1 or n == 2:
        org_count += 1
        return 1

    return original_fibo(n - 1) + original_fibo(n - 2)


memo = [0] * 41
dp_count = 0

def dp_fibo(n):
    global dp_count
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
        dp_count += 1
    return memo[n]

original_fibo(n)
dp_fibo(n)

print(org_count, dp_count)