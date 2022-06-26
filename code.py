import sys

n = int(input())
sequence_data = list(map(int, sys.stdin.readline().split()))
x = int(input())

count = 0
sequence_data.sort()

left = 0
right = n - 1
while left < right:
    sum = sequence_data[left] + sequence_data[right]
    if sum == x:
        count += 1
        left += 1
        right -= 1
    
    if sum < x:
        left += 1
    if sum > x:
        right -= 1

print(count)