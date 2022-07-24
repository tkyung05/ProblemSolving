import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

btn = [True] * 10

if m != 0: 
    error_btn = list(map(int, input().split()))
    for i in error_btn: btn[i] = False    

result = abs(n - 100) 
limit = 1000000

# 버튼을 눌러서 갈 수 있는 모든 경우의수를 탐색하여 최소값을 갱신 
for i in range(limit):
    num = str(i)
    bug = False

    for j in num:
        if not btn[int(j)]:
            bug = True
            break
    
    if not bug: result = min(abs(int(num) - n)  + len(num), result)

print(result)