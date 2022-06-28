import sys
data = list(sys.stdin.readline().split('-'))

result = []
for i in data:
    temp = list(map(int, i.split('+')))
    result.append(sum(temp))

ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]

print(ans)
