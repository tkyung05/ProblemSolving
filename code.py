from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = list(map(str, input().strip('\n')))
    n = int(input())
    data = deque(list(map(str, input().split(','))))

    if n > 0: 
        data[0] = data[0].strip('[')
        data[-1] = data[-1].strip(']\n')
    else:
        data = deque()
    
    direction = True # True = 오른쪽, False = 왼쪽
    bug = False

    for cm in cmd:
        if cm == 'R':
            if direction: direction = False
            else: direction = True
        
        elif cm == 'D':
            if len(data) == 0:
                print('error')
                bug = True
                break

            if direction: data.popleft()
            else: data.pop()
    
    if bug: continue

    if not direction: data.reverse()
    
    print('[' + ','.join(data) + ']')
