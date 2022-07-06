from cgi import print_arguments
from collections import deque

n = int(input())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)

while True:
    queue.popleft()
    if len(queue) == 1:
        break
    c = queue.popleft()
    queue.append(c)

print(queue.pop())