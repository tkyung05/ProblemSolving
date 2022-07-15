import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewels = [[] for _ in range(n)]
for i in range(n):
    jewels[i] = list(map(int, input().split()))

bags = [0] * k
for i in range(k):
    bags[i] = int(input())

jewels.sort()
bags.sort()

result = 0
choice_jews = []

for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(choice_jews, heapq.heappop(jewels)[1] * -1)
        
    if choice_jews:
        result += heapq.heappop(choice_jews)

print(result * -1)