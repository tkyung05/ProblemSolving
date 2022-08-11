import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpa = sorted(list(map(str, input().split())))

sequence = []
visited = [False] * C

vowel = {}
consonant = {}

for i in range(26):
    ap = chr(97 + i)
    if ap == 'a' or ap == 'e' or ap == 'i' or ap == 'o' or ap == 'u':
        vowel[ap] = True
    else: 
        consonant[ap] = True


def dfs(depth, idx):

    if depth == L:
        flag1, flag2 = False, 0
        
        for i in sequence:
            if i in vowel: flag1 = True
            elif i in consonant: flag2 += 1

        if flag1 and flag2 > 1:
            print(''.join(sequence))
            
        return

    for i in range(idx, C):
        if not visited[i]:
            visited[i] = True
            sequence.append(alpa[i])

            dfs(depth + 1, i)

            visited[i] = False
            sequence.pop()


dfs(0, 0)
