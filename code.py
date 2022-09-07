def solution(dartResult):
    answer = []
    
    option = {'*': 2, '#': -1}
    increase = {'S': 1, 'D': 2, 'T': 3}
    number = {str(i): i for i in range(10)}
    
    count = 0
    idx = 0
    
    while idx < len(dartResult):
        if dartResult[idx] in number:
            num = int(dartResult[idx])
            if dartResult[idx] == '1' and dartResult[idx + 1] == '0':
                num = 10
                idx += 1
                
            idx += 1
            answer.append(num ** increase[dartResult[idx]])
            idx += 1
            
            if idx < len(dartResult) and dartResult[idx] in option:
                if dartResult[idx] == '*':
                    if count != 0:
                        answer[count] = answer[count] * 2
                        answer[count - 1] = answer[count - 1] * 2
                    else:
                        answer[count] = answer[count] * 2
                else:
                    answer[count] = answer[count] * -1
                idx += 1
            
            count += 1
    
    return sum(answer)