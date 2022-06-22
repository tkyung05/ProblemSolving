n = int(input())
card_data = list(map(int, input().split()))
m = int(input())
get_data = list(map(int, input().split()))

result_dict = {card_data[i] : 1 for i in range(len(card_data))}

for i in range(len(get_data)):
    if get_data[i] in result_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')