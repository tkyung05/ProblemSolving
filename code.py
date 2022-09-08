def solution(n, k):
    answer = 0

    temp = ''
    while n:
        temp += str(n % k)
        n //= k

    numbers = temp[::-1].split('0')

    for number in numbers:
        prime = True

        if number == '' or number == '1':
            continue

        num = int(number)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            answer += 1

    return answer
