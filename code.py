import sys
input = sys.stdin.readline

n = int(input())
num_data = list(map(int, input().split()))
op_data = list(map(int, input().split()))

min_result = 1e9
max_result = -1e9

def dfs(count, total, plus, minus, mul, div):
    global min_result
    global max_result

    if count == n:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    if plus > 0:
        dfs(count + 1, total + num_data[count], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(count + 1, total - num_data[count], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(count + 1, total * num_data[count], plus, minus, mul - 1, div)
    if div > 0:
        dfs(count + 1, int(total / num_data[count]), plus, minus, mul, div - 1)


dfs(1, num_data[0], op_data[0], op_data[1], op_data[2], op_data[3])

print(max_result)
print(min_result)