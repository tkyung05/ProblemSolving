import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    input_files = list(map(int, input().split()))
    
    files = []
    for i in input_files:
        heapq.heappush(files, i)

    result = 0
    while len(files) > 1:
        one = heapq.heappop(files)
        two = heapq.heappop(files)
        
        new_file = one + two
        result += new_file 
        heapq.heappush(files, new_file)
    
    print(result)

    
