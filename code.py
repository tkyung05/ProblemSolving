import sys
from collections import Counter

T = int(input())
data = []
for i in range(T):
    data.append(int(sys.stdin.readline()))
data.sort()

print(round(sum(data) / T)) 
print(data[T // 2])

count_data = Counter(data).most_common()
if len(count_data) > 1 and count_data[0][1] == count_data[1][1]:
    print(count_data[1][0])
else:
    print(count_data[0][0])

print(data[T - 1] - data[0])
