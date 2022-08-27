def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(len(citations)):
        for i in range(len(citations)):
            if h + 1 <= citations[i] and len(citations) - i >= h + 1 and i <= h + 1:
                answer = h + 1
                break
    
    return answer