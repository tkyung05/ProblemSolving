import sys
input = sys.stdin.readline

n = int(input())

dough_price, topping_price = map(int, input().split())
dough_kcal = int(input())

topping_kcal = [0] * n
for i in range(n):
    topping_kcal[i] = int(input())
topping_kcal.sort(reverse=True)

re_price = dough_price
re_kcal = dough_kcal

result = dough_kcal / dough_price 
for k in topping_kcal:
    new_k = (re_kcal + k) / (re_price + topping_price)
    if result < new_k:
        result = new_k
        re_kcal += k 
        re_price += topping_price
    else:
        break

print(int(result))