from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

result = 0
 
for i in range(n):
    if result < data[i][0]:
        result = sum(data[i])
    else:    
        result += data[i][1]

print(result)