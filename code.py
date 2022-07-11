import sys
input = sys.stdin.readline

n = list(map(str, input()))

UCPC_data = ['U', 'C', 'P', 'C']
cur_index = 0
bug = True

for i in n:
    if i == UCPC_data[cur_index]:
        cur_index += 1
        if cur_index == 4:
            print('I love UCPC')
            bug = False
            break

if bug:
    print('I hate UCPC')
