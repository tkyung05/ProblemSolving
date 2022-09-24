LIMIT = 1000064


def solution(n):
    answer = 0
    compareNum = format(n, 'b').count('1')

    for num in range(n + 1, LIMIT + 1):
        if compareNum == format(num, 'b').count('1'):
            answer = num
            break

    return answer
