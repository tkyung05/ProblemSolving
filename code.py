answer = [0] * 2


def dfs(y, x, size, arr):
    global answer
    num = arr[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if arr[i][j] != num:
                dfs(y, x, size // 2, arr)
                dfs(y + size // 2, x, size // 2, arr)
                dfs(y, x + size // 2, size // 2, arr)
                dfs(y + size // 2, x + size // 2, size // 2, arr)
                return

    answer[num] += 1


def solution(arr):
    dfs(0, 0, len(arr), arr)
    return answer
