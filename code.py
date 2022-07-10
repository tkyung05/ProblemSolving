from collections import deque

n, k = map(int, input().split())

result = [0] * n
data = deque()

for i in range(1, n + 1):
    data.append(i)

for i in range(n):
    if i == n - 1:
        result[i] = data.popleft()
        break
         
    for j in range(k):
        pop_n = data.popleft()
        if j == k - 1:
            result[i] = pop_n
            break
        data.append(pop_n)

print('<', end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print(f'{result[i]}', end='')
    else:
        print(f'{result[i]},', end=' ')
print('>', end='')