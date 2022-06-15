import sys
T = int(input())

limit = 10000

eratos_data = [True] * (limit + 1)
eratos_data[0], eratos_data[1] = False, False

for i in range(2, int(len(eratos_data) ** 0.5)) :
    if eratos_data[i] :
        for j in range(i + i, len(eratos_data), i) :
            eratos_data[j] = False


for _ in range(T):
    n = int(sys.stdin.readline())
    min = 10000
    a, b = 0, 0
    r = 0

    for i in range(n // 2, n):
        r = n - i
        if eratos_data[i] and eratos_data[r]:
            if min > i - r:
                min = i - r
                a, b = r, i
    print (f'{a} {b}')