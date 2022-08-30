import math

def solution(fees, records):
    answer = []

    total_cars = {}
    total_times = {}
    total_fees = []
    
    for record in records:
        time, num, state = record.split()
        h, m = time.split(':')
        
        if state == 'IN':
            in_time = int(h) * 60 + int(m)
            total_cars[num] = in_time
            
        elif state == 'OUT':
            in_time = total_cars[num]
            out_time = int(h) * 60 + int(m)
            total_time = out_time - in_time
            
            if num not in total_times:
                total_times[num] = total_time
            else:
                total_times[num] += total_time
            total_cars[num] = -1
        
        
    for k in total_cars:
        if total_cars[k] != -1:
            in_time = total_cars[k]
            if k not in total_times:
                total_times[k] = (1439 - in_time)
            else:
                total_times[k] += (1439 - in_time)
        
    
    for k in total_times:
        fee = fees[1]
        if total_times[k] > fees[0]:
            fee += math.ceil((total_times[k] - fees[0]) / fees[2]) * fees[3]
        total_fees.append((int(k), fee))
        
    total_fees.sort()
    for n, f in total_fees:
        answer.append(f)
    
    return answer

