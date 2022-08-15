import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

comb = []
visited = [False] * n
result = int(1e9)

def dfs(depth, idx, team_size):
    global result

    if depth == team_size:
        link, start = 0, 0

        start_list = []
        for i in range(n):
            if not visited[i]:
                start_list.append(i)
        
        for i in range(team_size):
            for j in range(i, team_size):
                link += graph[comb[i]][comb[j]] + graph[comb[j]][comb[i]]
        
        for i in range(len(start_list)):
            for j in range(i, len(start_list)):
                start += graph[start_list[i]][start_list[j]] + graph[start_list[j]][start_list[i]]
        
        result = min(result, abs(link - start))
        return

    for i in range(idx, n):
        visited[i] = True
        comb.append(i)

        dfs(depth + 1, i + 1, team_size)
        
        visited[i] = False
        comb.pop()


for i in range(2, int(n//2) + 1):
    dfs(0, 0, i)
    if result == 0:
        break

print(result)
