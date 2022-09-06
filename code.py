def solution(s):
    answer = ''
    
    start_with = {'o' : ['ne'], 'z' : ['ero'], 't' : ['wo', 'hree'], 'f' : ['our', 'ive'],
             's' : ['ix', 'even'], 'e' : ['ight'], 'n' : ['ine']}
    
    found_number = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    idx = 0
    
    while idx < len(s):
        if s[idx] not in start_with:
            answer += s[idx]
            idx += 1
        else:
            for word in start_with[s[idx]]:
                if word[0] == s[idx + 1]:
                    answer += found_number[s[idx] + word]  
                    idx += len(word) + 1
                    break
            
    return int(answer)