from itertools import *

def solution(exp):
    answer = []
    oper_data = []
    expression = [ex for ex in exp]
    og_expression = []
    
    for i in range(len(expression)):
        if expression[i] == '*' or expression[i] == '-' or expression[i] == '+':
            oper_data.append(expression[i])
            expression[i] = '.'
    
    exp = ''  
    for ex in expression: exp += ex
    
    num_data = list(map(str, exp.split('.')))
    oper_com = list(permutations(set(oper_data), len(set(oper_data))))
    
    for i in range(len(num_data)):
        og_expression.append(num_data[i])
        if i != len(num_data) - 1:
            og_expression.append(oper_data[i])
    
    
    for com in range(len(oper_com)):
        temp = list(og_expression)
        
        for op in oper_com[com]:
            stack = []
            i = 0
            while i < len(temp):
                if temp[i] != op:
                    stack.append(temp[i])
                    i += 1
                else:
                    num_1 = int(stack.pop()) 
                    num_2 = int(temp[i + 1])
                    if temp[i] == '*':
                        stack.append(num_1 * num_2)
                    elif temp[i] == '+':
                        stack.append(num_1 + num_2)
                    elif temp[i] == '-':
                        stack.append(num_1 - num_2)
                    i += 2
            temp = list(stack)
            
        answer.append(abs(int(temp.pop())))
    
    return max(answer)