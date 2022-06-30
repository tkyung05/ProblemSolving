from collections import deque
import sys

n = int(sys.stdin.readline())
deque_data = deque()
for i in range(n):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'push_front':
        deque_data.appendleft(int(cmd[1]))
    
    elif cmd[0] == 'push_back':
        deque_data.append(int(cmd[1]))
    
    elif cmd[0] == 'pop_front':
        if deque_data:
            print(deque_data.popleft())
        else:
            print(-1)
    
    elif cmd[0] == 'pop_back':
        if deque_data:
            print(deque_data.pop())
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(deque_data))
    
    elif cmd[0] == 'empty':
        if deque_data:
            print(0)
        else:
            print(1)
    
    elif cmd[0] == 'front':
        if deque_data:
            print(deque_data[0])
        else:
            print(-1)
    
    elif cmd[0] == 'back':
        if deque_data:
            print(deque_data[-1])
        else:
            print(-1)