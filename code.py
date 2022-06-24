import sys
n = int(input())

stack = []
result = []
count = 1

def check_stack():
    global count
    for _ in range(n):
        num = int(sys.stdin.readline())

        while count <= num:
            stack.append(count)
            result.append("+")
            count += 1

        if stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            return True


if check_stack():
    print('NO')
else:
    for i in result:
        print(i)
