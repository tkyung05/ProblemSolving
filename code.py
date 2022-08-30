def solution(board, moves):
    answer = 0
    basket = []
    size = len(board)
    
    for num in moves:
        catch = 0
        
        for i in range(size):
            if board[i][num - 1] != 0:
                catch = board[i][num - 1]
                board[i][num - 1] = 0
                break
        
        if catch != 0:
            if basket and basket[-1] == catch:
                basket.pop()
                answer += 2
            else:
                basket.append(catch)            
    
    return answer
