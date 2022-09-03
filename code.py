def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    
    for c in cities:
        city = c.lower()
        hit, idx = False, 0
        
        for i in range(len(cache)):
            if cache[i] == city:
                hit = True
                idx = i
                break
        
        if hit:
            cache.append(cache.pop(idx))
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
            
    return answer