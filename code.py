import heapq
import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    d, n = map(int, input().split())
    data.append((d, n))
data.sort()

result = []
for day, noodle in data:
    heapq.heappush(result, noodle)

    if len(result) > day:
        heapq.heappop(result)

print(sum(result))