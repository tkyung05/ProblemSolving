import sys
n = int(sys.stdin.readline())
a = 60 * 5
b = 60
c = 10

a_count, b_count, c_count = 0, 0, 0

if n >= a:
    a_count += n // a
    n %= a

if n >= b:
    b_count += n // b
    n %= b

if n >= c:
    c_count += n // c
    n %= c

if n == 0:
    print(a_count, b_count, c_count)
else:
    print(-1)