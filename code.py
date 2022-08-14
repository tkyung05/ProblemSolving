import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack and tower[stack[-1]] <= tower[(n-1) - i]:
        result[stack.pop()] = n - i

    stack.append((n-1) - i)

print(*result)