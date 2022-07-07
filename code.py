import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num == 0:
        if not heap:
            print(0)
        else: 
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))
        
        
    
    