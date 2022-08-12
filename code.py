import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

sequence = []
visited = [False] * len(chicken)

result = int(1e9)

def dfs(depth, idx):
    global result

    if depth == m:
        dis_ch_house = [100] * len(house)

        for i in sequence:
            ch_y, ch_x = chicken[i][0], chicken[i][1]

            for j in range(len(house)):
                hs_y, hs_x = house[j][0], house[j][1]
                
                new_dis = abs(hs_y - ch_y) + abs(hs_x - ch_x)

                dis_ch_house[j] = min(dis_ch_house[j], new_dis)
        
        result = min(result, sum(dis_ch_house))
        return 

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)

            dfs(depth + 1, i)

            visited[i] = False
            sequence.pop()

dfs(0, 0)
print(result)