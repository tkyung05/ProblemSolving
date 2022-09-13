from collections import deque


def solution(people, limit):
    answer = 0
    people_weight = deque(sorted(people))

    while len(people_weight) > 1:
        if people_weight[0] + people_weight[-1] <= limit:
            people_weight.popleft()
            people_weight.pop()
        else:
            people_weight.pop()
        answer += 1

    return answer + len(people_weight)
