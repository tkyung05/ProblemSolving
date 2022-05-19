n = int(input())

honeyComb = 6
count = 1
result = 1

while True :
    if result >= n :
        break

    result += honeyComb * count
    count += 1

print(count)
