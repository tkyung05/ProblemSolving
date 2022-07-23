import sys
input = sys.stdin.readline

T = int(input())

def search_palin(string, r, l):
    while r < l:
        if string[r] != string[l]:
            return False
        r += 1
        l -= 1

    return True
        
    
for _ in range(T):
    string = list(map(str, input().strip('\n')))

    r, l = 0, len(string) - 1
    result = 0

    while r < l:
        if string[r] != string[l]:
            if search_palin(string, r + 1, l) or search_palin(string, r, l - 1):
                result = 1
                break
            else:
                result = 2
                break
        r += 1
        l -= 1
            
    print(result)
    
    
    