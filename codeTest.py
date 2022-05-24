import sys
T = int(input())

data = [[10], [1], [2, 4, 8, 6],
        [3, 9, 7, 1], [4, 6], [5], [6],
        [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

def f(a, b) :
    a %= 10
    b %= len(data[a])
    return data[a][b - 1]

for _ in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print(f(a, b))

