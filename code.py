import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input().strip('\n'))))

max_result = 1

def search():
    global max_result

    for i in range(n):
        w_count = 1
        h_count = 1
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1]:
                w_count += 1
                max_result = max(max_result, w_count)
            if graph[i][j] != graph[i][j + 1]:
                w_count = 1

            if graph[j][i] == graph[j + 1][i]:
                h_count += 1
                max_result = max(max_result, h_count)
            if graph[j][i] != graph[j + 1][i]:
                h_count = 1


for i in range(n):
    for j in range(n - 1):
        if graph[i][j] != graph[i][j + 1]:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            search()
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        if graph[j][i] != graph[j + 1][i]:
            graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]
            search()
            graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]

print(max_result)