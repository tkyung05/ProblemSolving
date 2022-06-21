import sys

n = int(input())
data = []

for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  data.append([x, y])
data.sort()

for i in range(n):
  print(data[i][0], data[i][1])

    
