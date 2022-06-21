import sys

n = int(input())
age_order_data = []
name_data = {}

for i in range(n):
  temp, name = sys.stdin.readline().split()
  age = int(temp)
  
  age_order_data.append((age, i))
  name_data.update({str(i) : name})

age_order_data.sort()

for i in range(len(age_order_data)):
  print(age_order_data[i][0], name_data[str(age_order_data[i][1])])


    
