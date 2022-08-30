def solution(numbers, hand):
    answer = []
    
    left_nums = {'1': (0, 0), '4': (1, 0), '7': (2, 0)}
    right_nums = {'3': (0, 2), '6': (1, 2), '9': (2, 2)}
    other_nums = {'2' : (0, 1), '5' : (1, 1), '8' : (2, 1), '0' : (3, 1)}
    
    now_left_pos = (3, 0)
    now_right_pos = (3, 2)
    
    for num in numbers:
        if str(num) in left_nums:
            now_left_pos = left_nums[str(num)]
            answer.append('L')
        elif str(num) in right_nums:
            now_right_pos = right_nums[str(num)]
            answer.append('R')
        else:
            dy, dx = other_nums[str(num)]
            l_y, l_x = now_left_pos
            r_y, r_x = now_right_pos
            
            left_gap = abs(dy - l_y) + abs(dx - l_x)
            right_gap = abs(dy - r_y) + abs(dx - r_x)
            
            if left_gap < right_gap:
                answer.append('L')
                now_left_pos = (dy, dx)
            elif left_gap > right_gap:
                answer.append('R')
                now_right_pos = (dy, dx)
            elif left_gap == right_gap:
                if hand == 'left':
                    answer.append('L')
                    now_left_pos = (dy, dx)
                else:
                    answer.append('R')
                    now_right_pos = (dy, dx)
        
        
    return ''.join(answer)