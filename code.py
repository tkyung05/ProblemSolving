import sys

n = int(input())
data = []
result_data = []

for i in range(n):
  data.append(sys.stdin.readline())
set_data = list(set(data))

for i in set_data:
  result_data.append((len(i), i))
result_data.sort()

for i in range(len(result_data)):
  print(result_data[i][1], end='')
    
