import sys

def check(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0 

        # 재귀로 주변 상하좌우 모두 호출하여 방문처리
        check(x - 1, y) 
        check(x + 1, y)
        check(x, y - 1)
        check(x, y + 1)
        # 킹각선..
        check(x - 1, y - 1) 
        check(x - 1, y + 1)
        check(x + 1, y - 1)
        check(x + 1, y + 1)

        # 처음 0 발견한 한번만 True 리턴
        return True
    # 1 이라면 그냥 False 리턴 
    return False



while True:
    w, h = map(int, sys.stdin.readline().split())
    
    if w + h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if check(i, j) == True:
                count += 1
    print(count)
