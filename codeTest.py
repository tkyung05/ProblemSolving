import sys

limit = 123456

eratos_data = [True] * (2 * limit + 1)
eratos_data[0], eratos_data[1] = False, False

for i in range(2, int(len(eratos_data) ** 0.5)) :
    if eratos_data[i] :
        for j in range(i + i, len(eratos_data), i) :
            eratos_data[j] = False


while True :
    n = int(sys.stdin.readline())
    count = 0
    if n == 0 :
        break

    if n == 1 :
        print(1)
        continue

    for i in range(n + 1, 2 * n) :
        if eratos_data[i] :
            count += 1

    print(count)





