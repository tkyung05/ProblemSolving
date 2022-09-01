def solution(s):
    result = []
    
    for alpha in list(s):
        if result and result[-1] == alpha:
            result.pop()
        else:
            result.append(alpha)
    
    return 0 if result else 1