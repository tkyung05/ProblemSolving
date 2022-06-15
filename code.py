import sys
T = int(input())

for _ in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline()) 
    F = [n for n in range(1, N + 1)]

    for _ in range(K):
        for i in range(1, N):
            F[i] += F[i - 1]
    print(F[-1])

    
