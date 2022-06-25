import sys
n = int(sys.stdin.readline())
A_data = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1] * n

for i in range(n):
    while len(stack) != 0 and A_data[stack[-1]] < A_data[i]:
        result[stack[-1]] = A_data[i]
        stack.pop()
        
    stack.append(i)

print(*result)