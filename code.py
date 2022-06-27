import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

result = 0
for i in range(n):
    result += sum(data)
    data.pop()
    
print(result)