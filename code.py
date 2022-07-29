import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

count_data = Counter(data)
result = [-1] * n

stack = []
for i in range(n):
    while stack and stack[-1][0] < count_data[data[i]]:
        result[stack.pop()[1]] = data[i]

    stack.append((count_data[data[i]], i))

print(' '.join(list(map(str,result))))