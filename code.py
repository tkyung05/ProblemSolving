def solution(dirs):
    answer = 0

    move = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    player_y, player_x = 5, 5
    overlap_way = {}

    for cmd in dirs:
        dy, dx = move[cmd]
        ny, nx = player_y + dy, player_x + dx

        if ny < 0 or ny > 10 or nx < 0 or nx > 10:
            continue

        key = str(player_y) + str(player_x) + str(ny) + str(nx)

        if key not in overlap_way:
            overlap_way[key] = 1
            overlap_way[str(ny) + str(nx) + str(player_y) + str(player_x)] = 1
            answer += 1

        player_y, player_x = ny, nx

    return answer
