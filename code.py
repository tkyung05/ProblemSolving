def solution(s):
    answer = []
    s = s[1:-1]
    
    transList = []
    idx = 0
    while idx < len(s):
        if s[idx] == '{':
            idx += 1
            start = idx
            while s[idx] != '}': idx += 1
            end = idx    
            
            data = s[start:end].split(',')
            transList.append((len(data), data))
            idx += 2
    transList.sort()
    
    answerHash = {}
    for l, data in transList:
        for element in data:
            if element not in answerHash:
                answerHash[element] = True
                answer.append(int(element))
    
    return answer






