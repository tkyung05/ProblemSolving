import sys
input = sys.stdin.readline

n = int(input())
h_data = list(map(int, input().split()))

h_memo = [0] * 1000001

result = 0
for i in h_data:
    if h_memo[i] == 0:
        h_memo[i - 1] = h_memo[i - 1] + 1
        result += 1
    
    elif h_memo[i] > 0:
        h_memo[i] = h_memo[i] - 1
        h_memo[i - 1] = h_memo[i - 1] + 1

print(result)  