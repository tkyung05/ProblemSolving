import sys
input = sys.stdin.readline

def bin_search(target): 
    left, right = 0, m - 1
    mid = (left + right) // 2

    while left <= right:
        if search_list[mid] == target:
            return True

        if search_list[mid] < target:
            left = mid + 1
        elif search_list[mid] > target:
            right = mid - 1
            
        mid = (right + left) // 2

    return False

        
n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

search_list = sorted(search)

result = {}
for i in range(n):
    if bin_search(card_list[i]):
        if card_list[i] in result:
            result[card_list[i]] += 1
        else:
            result[card_list[i]] = 1

for c in search:
    if c in result:
        print(result[c], end=' ')
    else:
        print(0, end=' ')
