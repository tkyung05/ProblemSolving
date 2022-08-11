import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
score = list(map(int, input().split()))

count = 0

sequence = []
visited = [False] * N

def dfs(depth, idx):
    global count
    
    if depth >= 2:
        if L <= sum(sequence) <= R and X <= abs(max(sequence) - min(sequence)):
            count += 1
        
        if depth == N:
            return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            sequence.append(score[i])

            dfs(depth + 1, i)

            visited[i] = False
            sequence.pop()

dfs(0, 0)
print(count)