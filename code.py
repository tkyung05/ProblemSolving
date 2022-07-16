import heapq
import sys
input = sys.stdin.readline

n = int(input())

test_score = []
for _ in range(n):
    test_score.append(tuple(map(int, input().split())))

test_score.sort()

result = []
for day, score in test_score:
    heapq.heappush(result, score)

    if len(result) > day:
        heapq.heappop(result)

print(sum(result))