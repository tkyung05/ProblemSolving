import sys
import heapq
input = sys.stdin.readline

n = int(input())

quest = []
for _ in range(n):
    p, d = map(int, input().split())
    quest.append((d, p))
quest.sort()

result = []
for i in range(n):
    day, point = quest[i]
    heapq.heappush(result, point)
    
    if len(result) > day:
        heapq.heappop(result)
    
print(sum(result))