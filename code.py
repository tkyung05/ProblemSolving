import sys
input = sys.stdin.readline

n = int(input())
data = list(map(str, input().strip('\n')))

eng = {}
for i in range(n): eng[chr(65+i)] = float(input())

postfix = []
for v in data:
    if v == '*' or v == '/' or v == '-' or v == '+': postfix.append(v)
    else: postfix.append(eng[v])

stack = []

for x in postfix:
    if x == '*':
        f = stack.pop()
        s = stack.pop()
        
        stack.append(s * f)
    elif x == '/':
        f = stack.pop()
        s = stack.pop()
        
        stack.append(s / f)
    elif x == '+':
        f = stack.pop()
        s = stack.pop()
        
        stack.append(s + f)
    elif x == '-':
        f = stack.pop()
        s = stack.pop()
        
        stack.append(s - f)
        
    else:   
        stack.append(float(x))

result = stack.pop()
print(f'{result:.2f}')