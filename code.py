import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    tree = list(map(int, input().split()))
    tree.sort()

    prev_one, prev_two = 0, 0
    one, two = 0, 1

    result = 0
    while two < n:
        if one == 0:
            result = max(result, abs(tree[one] - tree[two]))
        else:
            result = max(result, abs(tree[one] - prev_one), abs(tree[two] - prev_two))
        prev_one = tree[one]
        prev_two = tree[two]

        if two == (n - 2) and n % 2 == 1:
            result = max(result, abs(tree[one + 2] - prev_one))
            prev_one = tree[one + 2]

        one += 2
        two += 2 
    
    print(max(result, abs(prev_one - prev_two)))
    
        
    
    
