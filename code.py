import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]\

visited = [[0] * 5 for _ in range(5)]
result = 1

def check():
    count = 0
    rows = [0] * 5
    left_cross, right_cross = 0, 0

    for i in range(5):
        if sum(visited[i]) == 5:
            count += 1
        if visited[i][i] == 1:
            left_cross += 1
        if visited[i][4 - i] == 1:
            right_cross += 1
        
        for j in range(5):
            if visited[i][j] == 1:
                rows[j] += 1 
    
    if left_cross == 5:
        count += 1
    if right_cross == 5:
        count += 1
    for i in range(5):
        if rows[i] == 5: count += 1
    
    if count >= 3:
        return True
    else:
        return False


found_ans = False

for nums in ans:
    if found_ans: break
    for num in nums:

        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    visited[i][j] = 1
        
        if check(): 
            found_ans = True
            break

        result += 1

print(result)

