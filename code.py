import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    if n == 1:
        print(1)
        continue

    one_num = 1
    while True:
        one_num = one_num * 10 + 1
        
        if one_num % n == 0:
            break 
    
    print(len(str(one_num)))
    

        
        

