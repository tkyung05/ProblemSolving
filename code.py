def solution(x):
    return True if x % sum(list(map(int, list(map(str, x))))) == 0 else False


print(list(map(int, list(map(str, str(100))))))
print(solution(10))
