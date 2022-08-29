def solution(k, dungeons):
    answer = []
    visited = [False] * len(dungeons)
    
    def dfs(depth, now_p):
        answer.append(depth)
        
        if depth == len(dungeons):
            return
            
        for i in range(len(dungeons)):
            if not visited[i] and now_p >= dungeons[i][0]:
                visited[i] = True
                dfs(depth + 1, now_p - dungeons[i][1])
                visited[i] = False
        
    dfs(0, k)
    return max(answer)