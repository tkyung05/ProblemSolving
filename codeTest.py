n = int(input())
data = list(map(int, input().split()))
count = 0

for num in data :
    bug = False
    if num > 1 :
        for i in range(2, num - 1) :
            if num % i == 0 :
                bug = True
    else :
        bug = True

    if not bug :
        count += 1


print(count)
