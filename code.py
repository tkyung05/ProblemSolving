import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = list(map(str, input().strip('\n')))

visited = [False] * n
result = 0

for i in range(n):
    if graph[i] == 'P':
        start = i - k if i - k > 0 else 0
        end = i + k if i + k <= n - 1 else n - 1
        
        for j in range(start, end + 1):
            if graph[j] == 'H' and not visited[j]:
                visited[j] = True
                result += 1
                break

print(result)