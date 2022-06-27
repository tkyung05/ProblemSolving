import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append([b, a])
data.sort()

count = 0
point = 0
before_time = -1

for i in range(n):
    if data[i][1] >= before_time:
        before_time = data[i][0]
        count += 1
    else:
        continue
    
print(count)