import sys
input = sys.stdin.readline

k = int(input())
data = list(map(str, input().split()))

sequence = []
visited = [False] * 10

result = []

def dfs(depth):
    
    if depth > 1:
        if data[depth - 2] == '<':
            if not sequence[-2] < sequence[-1]:
                return 
        else:
            if not sequence[-2] > sequence[-1]:
                return

    if depth == k + 1:
        result.append(list(map(str, sequence)))
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)

            dfs(depth + 1)

            visited[i] = False
            sequence.pop()

dfs(0)   

print(''.join(result[-1]))
print(''.join(result[0]))
