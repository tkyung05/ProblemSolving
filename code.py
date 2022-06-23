n = int(input())
data = list(map(int, input().split()))
data.sort()

result = [0, 0]
cont_num = 2000000001

Left = 0
Right = len(data) - 1

while Left < Right:
    sum = data[Left] + data[Right]
    if abs(sum) < cont_num:
        cont_num = abs(sum)
        result[0], result[1] = data[Left], data[Right]

    elif sum < 0:
        Left += 1
    else:
        Right -= 1

if result[1] > result[0]:
    print(result[0], result[1])
else:
    print(result[1], result[0])
