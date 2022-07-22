import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(str, input().strip('\n'))))



b_and_w = [['B', 'W'], ['W', 'B']]
result = 64

def search_chess():
    global result

    b_count, w_count = 0, 0
    b_f, s = 1, 0

    for i in range(8):
        if b_f == 1: b_f, w_f = 0, 1
        else: b_f, w_f = 1, 0

        for j in range(8):
            if board[i][j] != b_and_w[b_f][s]:
                b_count += 1
            if board[i][j] != b_and_w[w_f][s]:
                w_count += 1

            if s == 1: s = 0
            else: s = 1
            
    result = min(result, b_count, w_count)


limit_h, limit_w = h - 8, w - 8
add_h, add_w = 0, 0

board = [[' '] * 8 for _ in range(8)]

while True:

    for i in range(8):
        for j in range(8):
            board[i][j] = graph[i + add_h][j + add_w]     
    search_chess()

    if add_w < limit_w:
        add_w += 1
    elif add_h < limit_h:
        add_h += 1
        add_w = 0
    else:
        break

print(result)