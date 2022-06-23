import sys
T = int(input())

for i in range(T):
    data = list(sys.stdin.readline())
    sum = 0
    for j in data:
        if j == "(":
            sum += 1
        if j == ")":
            sum -= 1
            if sum < 0:
                print("NO")
                break
        
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")