n = int(input())

result_data = []
not_found = False

for i in range(1, n):
    data = str(i)
    leng = len(data)
    div_list = []

    for j in range(leng):
        div_list.append(int(data[j]))

    if i + sum(div_list) == n:
        result_data.append(i)
        not_found = True

if not_found:
    result_data.sort()
    print(result_data[0])
else:
    print(0)
