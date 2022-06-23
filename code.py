import sys
T = int(input())

stack = []
for i in range(T):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop() 
    else:
        stack.append(num)

print(sum(stack))

        
    