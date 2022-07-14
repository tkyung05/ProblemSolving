import sys
input = sys.stdin.readline

limit = 1000000
eratos_data = [True] * (limit + 1)
eratos_data[0], eratos_data[1] = False, False

for i in range(2, int(len(eratos_data) ** 0.5)):
    if eratos_data[i]:
        for j in range(i + i, len(eratos_data), i):
            eratos_data[j] = False

prime_data = []
for i in range(2, len(eratos_data)):
    if eratos_data[i]:
        prime_data.append(i)

while True:
    n = int(input())

    if n == 0:
        break
    
    bug = True
    for i in prime_data:
        back = n - i
        if eratos_data[back] and back % 2 != 0:
            front = i
            bug = False
            break
    if bug:
        prime_data('Goldbach\'s conjecture is wrong.')
    else:
        print(f'{n} = {front} + {back}')