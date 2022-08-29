def solution(brown, yellow):
    
    def check_bug(overall, ny):
        if overall % ny != 0:
            return True
        return False
    
    answer = [0] * 2
    y, x = 3, 0
    overall_size = brown + yellow
    
    while True:
        if check_bug(overall_size, y):
            y += 1
            continue
        x = overall_size // y
        yellow_y = y - 2
        
        if check_bug(yellow, yellow_y):
            y += 1
            continue
        yellow_x = yellow // yellow_y
        
        if x - yellow_x == 2:
            answer[0], answer[1] = x, y 
            break
        else:
            y += 1
        
    return answer