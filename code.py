import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip('\n'))) for _ in range(n)]

result = 1

def check(size):
    global result

    for y in range((n - size) + 1):
        for x in range((m - size) + 1):
            if graph[y][x] == graph[y][x + (size - 1)] == graph[y + (size - 1)][x] == graph[y + (size - 1)][x + (size - 1)]:
                result = size
                return

for size in range(2, min(n, m) + 1):
    check(size)

print(result ** 2)