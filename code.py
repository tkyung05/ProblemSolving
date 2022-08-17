from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

emoji = [[0 for _ in range(n)] for _ in range(n + 1)]

def bfs():
    q = deque([(1, 0)])
    emoji[1][0] = 1
     
    while q:
        screen, clip = q.popleft()
        
        if screen == n:
            result = int(1e9)
            for i in emoji[n]:
                if i != 0: result = min(result, i)
            return result - 1

        if emoji[screen][screen] == 0:
            emoji[screen][screen] = emoji[screen][clip] + 1
            q.append((screen, screen))
        
        if clip != 0 and (screen + clip) <= n and emoji[screen + clip][clip] == 0:
            emoji[screen + clip][clip] = emoji[screen][clip] + 1
            q.append((screen + clip, clip))
        
        if (screen - 1) > 1 and emoji[screen - 1][clip] == 0:
            emoji[screen - 1][clip] = emoji[screen][clip] + 1
            q.append((screen - 1, clip))
        
print(bfs())