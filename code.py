import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kit = list(map(int, input().split()))

result = 0

sequence = []
visited = [False] * n

now_weight = 500

def dfs(depth):
    global result, now_weight

    if depth != 0:
        now_weight -= k
        now_weight += sequence[-1]
        
        if now_weight < 500:
            return 

    if depth == n:
        result += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sequence.append(kit[i])

            dfs(depth + 1)

            now_weight += k
            now_weight -= kit[i]

            visited[i] = False
            sequence.pop()

dfs(0)

print(result)