import sys
input = sys.stdin.readline

N = int(input())
nutrient = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
sequence = []

min_price = int(1e9)
min_set = []

def dfs(depth, idx):
    global min_price, min_set
    
    if depth >= 1:

        data = [0] * 5
        for i in sequence:
            for j in range(5):
                data[j] += graph[i][j]

        bug = False
        for i in range(4):
            if nutrient[i] > data[i]:
                bug = True
                break
        
        if not bug and min_price > data[4]:
            min_price = data[4]
            min_set = list(map(int, sequence))
            for i in range(depth): min_set[i] += 1

        if depth == N:
            return 

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)

            dfs(depth + 1, i)

            visited[i] = False
            sequence.pop()

dfs(0, 0)

if min_price == int(1e9):
    print(-1)
else:
    print(min_price)
    print(' '.join(list(map(str, min_set))))