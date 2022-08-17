import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

sequence = []
visited = [False] * n

result = int(1e9)

def dfs(depth, idx):
    global result
    
    if depth != 0:
        sour, bitter = data[sequence[0]][0], data[sequence[0]][1]

        for i in range(1, depth):
            sour *= data[sequence[i]][0]
            bitter += data[sequence[i]][1]

        result = min(result, abs(sour - bitter))
        
        if depth == n:
            return
    
    for i in range(idx, n):
        sequence.append(i)
        dfs(depth + 1, i + 1)
        sequence.pop()

dfs(0, 0)
print(result)