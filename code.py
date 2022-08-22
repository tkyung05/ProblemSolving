import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(k):
  y, x = map(int, input().split())
  graph[y - 1][x - 1] = 2

m = int(input())
dir_data = {}
for _ in range(m):
  sec, dir = input().split()
  dir_data[int(sec)] = dir

# 뱀 초기 값 세팅
snake_body = deque([(0, 0)])
snake_y, snake_x = 0, 0
snake_direct = 0
graph[0][0] = 1

def turn_snake(dir):
  global snake_direct

  if dir == 'L':
    snake_direct -= 1
  elif dir == 'D':
    snake_direct += 1
  snake_direct = (snake_direct % 4)

count = 0

while True:
  snake_y += dy[snake_direct]
  snake_x += dx[snake_direct]

  count += 1

  if snake_y < 0 or snake_y >= n or snake_x < 0 or snake_x >= n:
    break
  
  elif graph[snake_y][snake_x] == 2:
    graph[snake_y][snake_x] = 1
    snake_body.append((snake_y, snake_x))
    if count in dir_data:
      turn_snake(dir_data[count])
  
  elif graph[snake_y][snake_x] == 0:
    graph[snake_y][snake_x] = 1
    snake_body.append((snake_y, snake_x))
    cy, cx = snake_body.popleft()
    graph[cy][cx] = 0
    if count in dir_data:
      turn_snake(dir_data[count])
  
  else:
    break

print(count)