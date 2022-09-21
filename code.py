import heapq


def solution(n, works):
    data = []
    for work in works:
        heapq.heappush(data, -1 * work)

    while data[0] != 0 and n != 0:
        heapq.heappush(data, heapq.heappop(data) + 1)
        n -= 1

    answer = sum([num * num for num in data])
    return answer
