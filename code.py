import sys
import heapq

n = int(sys.stdin.readline())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])
data.sort()

end_time = []
heapq.heappush(end_time, data[0][1])

for i in range(1, n):
    if data[i][0] < end_time[0]:
        heapq.heappush(end_time, data[i][1])
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time, data[i][1])
    
print(len(end_time))
            
# blog 정리 해야겠다. 파이썬 우선순위 큐 heapq 모듈 사용법
# + 사용 이유  