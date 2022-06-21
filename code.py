import sys

n = int(input())
data = []

for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  data.append([y, x])
data.sort()

for i in range(n):
  print(data[i][1], data[i][0])

    
