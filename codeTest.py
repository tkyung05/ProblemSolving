a, b, v = map(int, input().split())

one_day = a - b
v -= a
count = 1

count += v // one_day

if v % one_day > 0 :
    count += 1

print(count)

