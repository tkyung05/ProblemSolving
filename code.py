def solution(files):
    answer = []
    num_check = {str(i): 1 for i in range(10)}
    order_files = []

    for idx in range(len(files)):
        h, n = '', ''

        num_start = 0
        for s in range(len(files[idx])):
            if files[idx][s] not in num_check:
                h += files[idx][s]
            else:
                num_start = s
                break

        for s in range(num_start, len(files[idx])):
            if files[idx][s] in num_check and (s - num_start) < 5:
                n += files[idx][s]
            else:
                break

        order_files.append((h.lower(), int(n), idx))

    order_files.sort()
    for h, n, idx in order_files:
        answer.append(files[idx])

    return answer
