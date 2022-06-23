import sys

def str_check(data):
    for i in range(len(list(data))):
        # 소괄호 조건
        if data[i] == '(':
            stack.append('(')

        elif data[i] == ')':
            if len(list(stack)) == 0:
                return 'no'
            elif len(list(stack)) != 0:
                if stack[-1] == '[':
                    return 'no'
                else:
                    stack.pop()
                

        # 대괄호 조건 
        elif data[i] == '[':
            stack.append('[')

        elif data[i] == ']':
            if len(list(stack)) == 0:
                return 'no'
            elif len(list(stack)) != 0:
                if stack[-1] == '(':
                    return 'no'
                else:
                    stack.pop()

        # 기타 문자열 넘기기
        else:
            continue

    if len(list(stack)) == 0:
        return 'yes'
    else:
        return 'no'
    
    


while True:
    data = sys.stdin.readline()
    if data[0] == '.' and data[1] == '\n':
        break 

    stack = []
    print(str_check(data))
    
    
