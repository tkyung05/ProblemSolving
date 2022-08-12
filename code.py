import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0: blank.append((i, j))


def possible(y, x):
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sy, sx = (y // 3) * 3, (x // 3) * 3
    for i in range(sy, sy + 3):
        for j in range(sx, sx + 3):
            if graph[i][j] in possible_nums:
                possible_nums.remove(graph[i][j])
    
    for i in range(9):
        if graph[i][x] in possible_nums: 
            possible_nums.remove(graph[i][x])
        if graph[y][i] in possible_nums: 
            possible_nums.remove(graph[y][i])

    return possible_nums


def dfs(depth):

    if depth == len(blank):
        for i in range(9): print(*graph[i])
        exit(0)

    
    blank_y, blank_x = blank[depth][0], blank[depth][1] 
    possible_list = possible(blank_y, blank_x)

    for i in possible_list:
        graph[blank_y][blank_x] = i
        dfs(depth + 1)
        graph[blank_y][blank_x] = 0

dfs(0)