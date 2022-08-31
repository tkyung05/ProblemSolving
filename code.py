def solution(new_id):
    answer = ''
    not_possible = {'/': 1, '~': 1, '!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '=': 1, '+': 1, '[': 1, ']': 1, '{': 1, '}': 1, ':': 1, '?': 1, ',': 1, '<': 1, '>': 1}
    
    one_step = new_id.lower()
    two_step = ''
    for i in one_step:
        if i in not_possible: continue
        else: two_step += i
    
    three_step = ''
    for i in two_step:
        if len(list(three_step)) != 0 and three_step[-1] == '.' and i == '.': continue
        else: three_step += i
    
    if len(list(three_step)) != 0:
        if three_step[0] == '.':
            three_step = three_step[1:]
        if len(list(three_step)) != 0 and three_step[-1] == '.':
            three_step = three_step[:len(list(three_step)) - 1]

    if len(list(three_step)) == 0:
        three_step = 'a'
    
    if len(list(three_step)) >= 16:
        three_step = three_step[:15] 
        if three_step[-1] == '.':
            three_step = three_step[:14]
            
    if len(list(three_step)) <= 2:
        three_step += three_step[-1] * (3 - len(list(three_step)))
        
    return three_step



