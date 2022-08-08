import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def cut_paper(y, x, n):

    color = paper[y][x]
    
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != paper[i][j]:

                cut_size = n // 3
                cut_paper(y, x, cut_size)
                
                cut_paper(y + cut_size, x, cut_size)
                cut_paper(y + cut_size * 2, x, cut_size)
                
                cut_paper(y, x + cut_size, cut_size)
                cut_paper(y, x + cut_size * 2, cut_size)
               
                cut_paper(y + cut_size, x + cut_size, cut_size) 
                cut_paper(y + cut_size, x + cut_size * 2, cut_size)
                
                cut_paper(y + cut_size * 2, x + cut_size, cut_size)
                cut_paper(y + cut_size * 2, x + cut_size * 2 , cut_size)

                return
    
    result.append(color)

         
        
cut_paper(0, 0, N)

print(result.count(-1))
print(result.count(0))
print(result.count(1))