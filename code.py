import sys
input = sys.stdin.readline

king, stone, n = map(str, input().split())

move = {}
move['R'] = (0, 1)
move['L'] = (0, -1)
move['B'] = (-1, 0)
move['T'] = (1, 0)
move['RT'] = (1, 1)
move['LT'] = (1, -1)
move['RB'] = (-1, 1)
move['LB'] = (-1, -1)


king_pos_y, king_pos_x = int(king[1]) - 1, ord(king[0]) - 65
stone_pos_y, stone_pos_x = int(stone[1]) - 1, ord(stone[0]) - 65


for _ in range(int(n)):
    cmd = input().strip('\n')
    
    dy, dx = move[cmd]
    
    king_ny, king_nx = king_pos_y + dy, king_pos_x + dx

    if king_ny < 0 or king_ny >= 8 or king_nx < 0 or king_nx >= 8:
        continue
    
    if king_ny == stone_pos_y and king_nx == stone_pos_x:
        stone_ny, stone_nx = stone_pos_y + dy, stone_pos_x + dx

        if stone_ny < 0 or stone_ny >= 8 or stone_nx < 0 or stone_nx >= 8:
            continue 
        stone_pos_y, stone_pos_x = stone_ny, stone_nx

    king_pos_y, king_pos_x = king_ny, king_nx 


print(chr(65 + king_pos_x) + str(king_pos_y + 1))
print(chr(65 + stone_pos_x) + str(stone_pos_y + 1))
