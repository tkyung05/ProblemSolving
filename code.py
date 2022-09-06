def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a, b = format(arr1[i], 'b'), format(arr2[i], 'b')
        temp = str(int(a) + int(b))
        temp = '0' * (n - len(temp)) + temp 
        
        row = []
        for i in temp:
            if i == '0': row.append(' ')
            else: row.append('#')
        
        answer.append(''.join(row))
        
        
    return answer