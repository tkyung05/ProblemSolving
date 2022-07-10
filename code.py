n = int(input())

count = 666
result = 0
while True:
    if '666' in str(count):
        result += 1
        if result == n:
            print(count)
            break
        count += 1
    else:
        count += 1