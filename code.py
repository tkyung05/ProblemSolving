def solution(survey, choices):
    answer = ''
    mbti_score = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    mbti = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    for i in range(len(choices)):
        if choices[i] > 4:
            mbti_score[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            mbti_score[survey[i][0]] += abs(choices[i] - 4) 
    
    for i in range(4):
        temp = []
        temp.append((mbti_score[mbti[i][0]], mbti[i][0]))
        temp.append((mbti_score[mbti[i][1]], mbti[i][1]))
        temp.sort(reverse=True)
        if temp[0][0] == temp[1][0]:
            answer += temp[1][1]
        else: 
            answer += temp[0][1]
            
    return answer