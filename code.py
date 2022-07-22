import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

result = 0
limit = [15, 28, 19]
data = [0, 0, 0]

while True:
    if data[0] == e and data[1] == s and data[2] == m:
        break
    
    for i in range(3):
        data[i] = data[i] + 1
        if data[i] > limit[i]:
            data[i] = 1

    result += 1

print(result)