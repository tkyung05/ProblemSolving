def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = format(num, 'b')
        if len(bin_num) == sum(list(map(int, bin_num))):
            bin_num = '0b10' + bin_num[1:]
        else:
            bin_list = list(bin_num)
            for i in range(len(bin_list) - 1, -1, -1):
                if bin_list[i] == '0':
                    bin_list[i] = '1'
                    for j in range(i + 1, len(bin_list)):
                        if bin_list[j] == '1':
                            bin_list[j] = '0'
                            break
                    break
            bin_num = '0b' + ''.join(bin_list)

        answer.append(int(bin_num, 2))

    return answer
