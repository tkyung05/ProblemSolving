from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, graph):
    visited = [[0] * 5 for _ in range(5)]
    visited[y][x] = 1
    q = deque([(y, x)])
    
    while q:
        y, x = q.popleft()

        if 1 < visited[y][x] < 4 and graph[y][x] == 'P':
            return True
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny > 4 or nx < 0 or nx > 4:
                continue
            if graph[ny][nx] == 'X':
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    
    return False
    


def solution(places):
    answer = [0] * 5
    
    for i in range(5):
        bug = 1
        for y in range(5):
            for x in range(5):
                if places[i][y][x] == 'P':
                    if bug == 1 and bfs(y, x, places[i]):
                        bug = 0
        answer[i] = bug
        
    return answer





