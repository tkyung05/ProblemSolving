import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().strip('\n')))

result = []
for i in range(n):
    while k > 0 and result:
        if result[-1] < data[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(data[i])
    
for i in range(len(result) - k):
    print(result[i], end='')
