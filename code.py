n = int(input())
num_data = list(map(int, input().split()))

set_data = sorted(set(num_data))
dic_data = {set_data[i] : i for i in range(len(set_data))}

for i in num_data:
  print(dic_data[i], end=' ')
  