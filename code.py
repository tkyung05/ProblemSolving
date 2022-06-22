import sys
n = int(input())

i = 0
stack = []

def push(num):
    stack.append(int(num))
    global i
    i += 1

def pop():
    global i
    if len(stack) != 0:
        print(stack.pop(i - 1))
        i -= 1
    else:
        print(-1)

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[i - 1])
    else:
        print(-1)

for _ in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "push":
        push(cmd[1])
    if cmd[0] == "pop":
        pop()
    if cmd[0] == "size":
        print(len(stack))
    if cmd[0] == "empty":
        empty()
    if cmd[0] == "top":
        top()