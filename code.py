import sys
n = int(sys.stdin.readline())

ordinary_data = []
zero_data = []
minus_data = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        zero_data.append(num)
    elif num < 0:
        minus_data.append(num)
    elif num > 0:
        ordinary_data.append(num)

minus_data.sort()
ordinary_data.sort(reverse=True)

# kim_tk. 스파게티 코드 씹팔 ㅋ 

# 자연수 데이터를 전부 묶거나 더해줌
result = 0
for i in range(0, len(ordinary_data), 2):
    if i == len(ordinary_data) - 1:
        result += ordinary_data[i]
        break

    if ordinary_data[i] == 1 or ordinary_data[i + 1] == 1:
        result += ordinary_data[i] + ordinary_data[i + 1]    
        continue  

    result += ordinary_data[i] * ordinary_data[i + 1]


# 음수 데이터를 전부 묶거나 더해줌
if len(minus_data) != 0:
    for i in range(0, len(minus_data), 2):
        if i == len(minus_data) - 1:
            if len(zero_data) == 0:
                result += minus_data[i]
            break
        result += minus_data[i] * minus_data[i + 1]

print(result)