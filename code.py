import sys
input = sys.stdin.readline

main_editor = list(map(str, input().strip('\n')))
n = int(input())

side_editor = []

for _ in range(n):
    cmd = list(map(str, input().split()))

    if cmd[0] == 'P':
        main_editor.append(cmd[1])
    elif cmd[0] == 'L' and main_editor:
        side_editor.append(main_editor.pop())
    elif cmd[0] == 'D' and side_editor:
        main_editor.append(side_editor.pop())
    elif cmd[0] == 'B' and main_editor:
        main_editor.pop()

if side_editor:
    side_editor.reverse()

print(''.join(main_editor) + ''.join(side_editor))