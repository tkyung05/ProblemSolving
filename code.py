def solution(m, n, data):
    answer = 0
    board = [list(map(str, i)) for i in data]
    
    while True:
        pop_count = 0
        visited = [[0] * n for _ in range(m)]
        
        # 블록 터트리기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == 'EMPTY': continue
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    visited[i][j], visited[i + 1][j], visited[i + 1][j + 1], visited[i][j + 1] = 1, 1, 1, 1           
        
        # 터진 블록 개수 카운드
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    pop_count += 1
                    board[i][j] = 'EMPTY'
    
        # 종료 조건
        if pop_count == 0:
            break
        
        # 블록 떨어지는 기능
        for i in range(n):
            for j in range(m - 1, 0, -1):
                if board[j][i] == 'EMPTY':
                    for k in range(j - 1, -1, -1):
                        if board[k][i] != 'EMPTY':
                            board[j][i] = board[k][i]
                            board[k][i] = 'EMPTY'
                            break
        
        answer += pop_count 
                    
    return answer