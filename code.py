import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
oper_count = list(map(int, input().split()))

min_result = int(1e9)
max_result = int(-1e9)

sequence = []

overlap_oper = {}

def dfs(depth, plus, minus, mult, div, total):
    global max_result, min_result
    
    if depth == (n - 1):
        max_result = max(max_result, total)
        min_result = min(min_result, total) 
        return

    if plus > 0:
        dfs(depth + 1, plus - 1, minus, mult, div, total + num[depth + 1])
    if minus > 0:
        dfs(depth + 1, plus, minus - 1, mult, div, total - num[depth + 1])
    if mult > 0:
        dfs(depth + 1, plus, minus, mult - 1, div, total * num[depth + 1])
    if div > 0:
        dfs(depth + 1, plus, minus, mult, div - 1, int(total // num[depth + 1]))


dfs(0, oper_count[0], oper_count[1], oper_count[2], oper_count[3], num[0])

print(max_result)
print(min_result)