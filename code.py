def solution(msg):
    answer = []
    dictionary = {}
    
    for i in range(1, 27): dictionary[chr(64 + i)] = i
    dic_idx, idx = 27, 0
    end = False
    
    while True:
        wc = msg[idx]
        next_idx = 0
        
        for i in range(idx + 1, len(msg)):
            wc += msg[i]
            next_idx += 1
            if wc not in dictionary: break
            elif i == len(msg) - 1: end = True
            
        if end or idx == len(msg) - 1:
            answer.append(dictionary[wc])
            break
            
        w = wc[:len(wc) - 1]
        answer.append(dictionary[w])
        dictionary[wc] = dic_idx
        
        dic_idx += 1
        idx += next_idx
        
    return answer