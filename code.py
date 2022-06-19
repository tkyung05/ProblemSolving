import sys

T = int(input())
x_data = []
y_data = []
rank_data = []

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    x_data.append(x)
    y_data.append(y)

for i in range(T):
    count = 1
    for j in range(T):
        if x_data[j] > x_data[i] and y_data[j] > y_data[i]:
            count += 1
    rank_data.append(count)

print(*rank_data)
