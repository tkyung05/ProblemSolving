import sys
input = sys.stdin.readline

n = int(input())
alpa_data = [list(map(str, input().strip('\n'))) for _ in range(n)]

dict_alpa = {}

# 각 알파벳의 현재 위치에 따라 10의 제곱으로 크기를 정하고, 알파벳의 종류에 따라 dict에 저장 또는 더함
for word in alpa_data:
    leng = len(word) - 1

    for k in word:
        if k in dict_alpa:
            dict_alpa[k] += 10 ** leng
        else:
            dict_alpa[k] = 10 ** leng
        leng -= 1

# 위에서 정한 값이 클 수록 우선 순위가 높아지기 때문에 내림차순 정렬
data = sorted(dict_alpa.values(), reverse=True)

# 우선 순위에 따라 9, 8, 7... 순으로 곱해줌
result, num = 0, 9
for i in data:
    result += i * num
    num -= 1

print(result)