LIMIT = 100001
notationNums = []


def transNotation(num, n):
    global notationNums
    result = []

    if num == 0:
        result.append(0)

    while num > 0:
        if num % n < 10:
            result.append(num % n)
        else:
            result.append(chr(num % n - 10 + ord('A')))
        num //= n

    notationNums += result[::-1]


def solution(n, t, m, p):
    answer = ''
    p -= 1

    for num in range(LIMIT):
        transNotation(num, n)
        if len(notationNums) >= m * t:
            break

    for _ in range(t):
        answer += str(notationNums[p])
        p += m

    return answer
