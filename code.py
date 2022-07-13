import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

temp = list(map(int, input().split()))

card = []
for i in temp:
    heapq.heappush(card, i)

for i in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)

    sum_num = a + b
    heapq.heappush(card, sum_num)
    heapq.heappush(card, sum_num)

print(sum(card))