import heapq
import sys

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0

while len(heap) > 1:
    f_card = heapq.heappop(heap)
    s_card = heapq.heappop(heap)
    
    temp = f_card + s_card
    result += temp
    heapq.heappush(heap, temp)

print(result)
    
    



