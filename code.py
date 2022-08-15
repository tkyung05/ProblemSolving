from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    for i in range(n): queue[i] = (i, queue[i])
    
    count = 1
    while True:
        idx, num = queue.popleft()
            
        bug = False
        for i in range(len(queue)):
            if num < queue[i][1]:
                bug = True
                break
        
        if bug: 
            queue.append((idx, num))
        else:
            if idx == m: 
                print(count)
                break
            count += 1
    
