def solution(s):
    answer = [0] * 2

    delZero, trans = 0, 0
    while len(s) > 1:
        countOne = sum(list(map(int, s)))
        delZero += len(s) - countOne
        s = format(countOne, 'b')
        trans += 1

    answer[0], answer[1] = trans, delZero
    return answer
