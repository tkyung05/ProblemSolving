def solution(N, stages):
    answer = []
    result = []
    
    for now_stage in range(1, N + 1):
        fail_players = 0
        all_players = 0
        
        for stage in stages:
            if now_stage <= stage:
                all_players += 1        
            if now_stage == stage:  
                fail_players += 1

        if all_players == 0:
            total = 0
        else: 
            total = fail_players / all_players
        result.append((total, -1 * now_stage))
    
    result.sort(reverse=True)
    
    for value, idx in result:
        answer.append(-1 * idx)

    return answer