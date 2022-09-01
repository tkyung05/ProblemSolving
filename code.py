def solution(s):
    answer = []
    if len(s) == 1: return 1
    
    for cut_size in range(1, len(s) // 2 + 1):
        overlap_count = 1
        result = ''
        prev_str = s[:cut_size]
        
        
        for start in range(cut_size, len(s), cut_size):
            if prev_str == s[start : start + cut_size]:
                overlap_count += 1
            else:
                if overlap_count > 1:
                    result += str(overlap_count) + prev_str
                else:
                    result += prev_str
                    
                prev_str = s[start : start + cut_size]
                overlap_count = 1
                
        if overlap_count > 1:
            result += str(overlap_count) + prev_str
        else:
            result += prev_str
            
        answer.append(len(result))
        
    return min(answer)