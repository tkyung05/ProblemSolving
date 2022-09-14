def solution(land):

    for i in range(1, len(land)):
        for j in range(4):
            prev_max = -1
            for k in range(4):
                if k != j:
                    prev_max = max(prev_max, land[i - 1][k])
            land[i][j] += prev_max

    return max(land[-1])
