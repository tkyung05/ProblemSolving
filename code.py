from random import randrange
import sys
import heapq

n = int(sys.stdin.readline())
data = []
for i in range(n):
    num = (int(sys.stdin.readline()) * -1)
    if num * -1 > 0:
        heapq.heappush(data, num)
    else:
        if len(data) == 0:
            print(0)
        else:
            print(heapq.heappop(data) * -1)