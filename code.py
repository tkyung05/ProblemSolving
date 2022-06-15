import sys
T = int(input())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    result = 0  

    if N % H == 0:
        result = (H * 100) + (N // H)
    else :
        result = (N % H * 100) + (N // H + 1)

    print(result)

    
