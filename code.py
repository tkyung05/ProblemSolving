from itertools import *

def solution(orders, course):
    answer = []

    max_of_size = {}
    possible_menu = {}

    for o in orders:
        order = sorted(list(map(str, o)))
        for size in range(2, len(order) + 1):
            for com in combinations(order, size):
                menu = ''.join(list(com))
                if menu in possible_menu:
                    possible_menu[menu][0] += 1
                else:
                    possible_menu[menu] = [1, size] 

                if size in max_of_size:
                    max_of_size[size] = max(max_of_size[size], possible_menu[menu][0])
                else:
                    max_of_size[size] = possible_menu[menu][0]

    for num in course:
        if num not in max_of_size or max_of_size[num] == 1:
            continue
        for menu in possible_menu:
            if possible_menu[menu][1] == num and possible_menu[menu][0] == max_of_size[num]:
                answer.append(menu) 
  
    return sorted(answer)