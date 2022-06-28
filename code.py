limit = 7368787
eratos_data = [True] * (limit + 1)
eratos_data[0], eratos_data[1] = False, False

for i in range(2, int(len(eratos_data) ** 0.5)):
    if eratos_data[i]:
        for j in range(i + i, len(eratos_data), i):
            eratos_data[j] = False

count = 0
n = int(input())
for i in range(len(eratos_data)):
    if eratos_data[i]:
        count += 1
        if count == n:
            print(i)
            break
