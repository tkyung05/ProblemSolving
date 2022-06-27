import sys
n = int(sys.stdin.readline())
a_data = list(map(int, sys.stdin.readline().split()))
b_data = list(map(int, sys.stdin.readline().split()))

a_data.sort()
b_data.sort(reverse=True)

result = 0
for i in range(n):
    result += a_data[i] * b_data[i]

print(result)