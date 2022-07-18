import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    w, p = map(int, input().split())
    data.append((p, w * -1))
data.sort()

sum_weight, same_price = 0, 0
result = []

for i in range(len(data)):
    p, w = data[i]

    sum_weight += w * -1

    if i > 0 and p == data[i - 1][0]:
        same_price += p
    else:
        same_price = p

    if sum_weight >= m:
        result.append(same_price)
        
        if same_price == p:
            break
    
if sum_weight < m:
    print(-1)
else:
    print(min(result))