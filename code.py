import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

m = int(sys.stdin.readline())
target_data = list(map(int, sys.stdin.readline().split()))

def bin_search(target, start, end):
    if start > end:
        return print(0)
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return print(1)

    elif data[mid] < target:
        bin_search(target, mid + 1, end)
    elif data[mid] > target:
        bin_search(target, start, mid - 1)


for i in target_data:
    bin_search(i, 0, n - 1)