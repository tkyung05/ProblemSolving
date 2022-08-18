import sys
input = sys.stdin.readline

n = int(input())

while True:
    if n == 1:
        n += 1
        continue

    num = list(str(n))
    left, right = 0, len(num) - 1
        
    isFalin = True
    isPrime = True

    while left < right:
        if num[left] != num[right]:
            isFalin = False
            break
        left += 1
        right -= 1

    if isFalin:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: 
                isPrime = False
                break
    
    if isPrime and isFalin:
        print(n)
        break

    n += 1

