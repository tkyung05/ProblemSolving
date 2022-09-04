def solution(n, k, cmd):
    answer = ['O'] * n
    graph = {i : [i - 1, i + 1] for i in range(n)}
    graph[0][0], graph[n - 1][1] = None, None
    
    save_z = []
    now_select = k
    
    for i in range(len(cmd)):
        c = cmd[i].split()
    
        if c[0] == 'C':
            answer[now_select] = 'X'
            prev, next = graph[now_select]
            save_z.append([now_select, prev, next])
            
            if next == None:
                now_select = prev
            else:
                now_select = next
            
            if prev == None:
                graph[next][0] = None
            elif next == None:
                graph[prev][1] = None
            else:
                graph[prev][1] = next
                graph[next][0] = prev
        
        elif c[0] == 'Z':
            now_idx, prev, next = save_z.pop()
            answer[now_idx] = 'O'
            
            if prev == None:
                graph[next][0] = now_idx
            elif next == None:
                graph[prev][1] = now_idx
            else:
                graph[prev][1] = now_idx
                graph[next][0] = now_idx

        else:
            x = int(c[1])           
            key = 0 if c[0] == 'U' else 1
                
            for _ in range(x):
                now_select = graph[now_select][key]
            
            
    return ''.join(answer)








