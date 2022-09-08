def solution(n, words):
    answer = [0] * 2
    overlapCheck = {}

    if len(words[0]) == 1:
        return [1, 1]

    prev_word = words[0][-1]
    overlapCheck[words[0]] = True

    for i in range(1, len(words)):
        if len(words[i]) > 1 and words[i][0] == prev_word and words[i] not in overlapCheck:
            overlapCheck[words[i]] = True
            prev_word = words[i][-1]
        else:
            answer[0] = (i % n) + 1
            answer[1] = (i + 1) // n
            answer[1] += 1 if (i + 1) % n != 0 else 0
            break

    return answer
