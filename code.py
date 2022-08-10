import sys
input = sys.stdin.readline

T = int(input())

operator = [' ', '+', '-']
sequence = []

def dfs(depth):

    if depth == n - 1:
        total = ['1']
        result = ['1']
        
        for i in range(n - 1):
            now_num = str(i + 2)

            if sequence[i] == ' ':
                total[-1] = str(total[-1] + now_num)
                result.append(' ')
            elif sequence[i] == '+':
                total.append(now_num)
                result.append('+')
            elif sequence[i] == '-':
                total.append(str('-' + now_num)) 
                result.append('-')
            
            result.append(now_num)

        if sum(list(map(int, total))) == 0:
            print(''.join(result))
            
        return 

    for i in operator:
        sequence.append(i)
        dfs(depth + 1)
        sequence.pop()


for _ in range(T):
    n = int(input())

    dfs(0)
    print()