import heapq

def solution(operations):
    answer = [0] * 2
    
    min_heap = []
    max_heap = []
    visited = [False] * 1000000
    
    for i in range(len(operations)):
        cmd, num = operations[i].split()
        
        if cmd == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-1 * int(num), i))
            
            visited[i] = True
        
        else:
            if num == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    number, idx = heapq.heappop(min_heap)
                    visited[idx] = False
            
            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    number, idx = heapq.heappop(max_heap)
                    visited[idx] = False
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    
    if len(min_heap) == 0 or len(max_heap) == 0:
        return answer
    else:
        answer[0] = heapq.heappop(max_heap)[0] * -1
        answer[1] = heapq.heappop(min_heap)[0]
        return answer






