from random import randrange
from unittest import result


n = input()

result_list = []
for i in range(len(list(n))):
    result_list.append(int(n[i]))
result_list.sort(reverse=True)

for i in result_list:
    print(i, end='')


