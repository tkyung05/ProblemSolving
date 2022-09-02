import math

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    
    
    str1_hash = {}
    str2_hash = {}
    intersection_elements = {}
    
    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90:
            element = str1[i] + str1[i + 1]
            if element not in str1_hash:
                str1_hash[element] = 1
            else:
                str1_hash[element] += 1

    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90:
            element = str2[i] + str2[i + 1]
            if element in str1_hash:
                intersection_elements[element] = True
            if element not in str2_hash:
                str2_hash[element] = 1
            else:
                str2_hash[element] += 1

                
    
    all_elements = set([k for k in str1_hash] + [k for k in str2_hash])
    union, intersection = 0, 0

    for e in all_elements:
        max_num = 0
        if e in str1_hash:
            max_num = str1_hash[e]
        if e in str2_hash:
            max_num = max(max_num, str2_hash[e])
        union += max_num
        
    for e in intersection_elements:
        min_num = 0
        if e in str1_hash:
            min_num = str1_hash[e]
        if e in str2_hash:
            min_num = min(min_num, str2_hash[e])
        intersection += min_num
    
    if intersection + union == 0:
        intersection, union = 1, 1
    
    answer = math.trunc((intersection / union) * 65536)
    return answer





