import sys
input = sys.stdin.readline

a, b = map(str, input().split())

B = int(b)

data = list(map(int, a))
sequence = []
visited = [False] * len(data)

result = -1

def dfs(depth):
    global result
    
    if depth == len(data):
        total = int(''.join(sequence))

        if total < B:
            result = max(result, total)
        return

    for i in range(len(data)):
        if not visited[i]:
            if depth == 0 and data[i] == 0:
                continue

            visited[i] = True
            sequence.append(str(data[i]))

            dfs(depth + 1)

            visited[i] = False
            sequence.pop()

dfs(0)
print(result)