import sys
T = int(input())

for i in range(T):
    data = list(sys.stdin.readline().split())
    for j in range(len(data)):
        if j == int(len(data) - 1):
            print(data[j][::-1])
        else :
            print(data[j][::-1], end=' ')