import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

overlap_data = {}
for _ in range(n):
    overlap_data[str(input().strip('\n'))] = 1

for _ in range(m):
    i = str(input().strip('\n'))
    if i in overlap_data:
        result.append(i)

result.sort()

print(len(result))
for i in result:
    print(i)
        
