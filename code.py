import sys
input = sys.stdin.readline

n = int(input())
crains = list(map(int, input().split()))
k = int(input())
boxs = list(map(int, input().split()))

crains.sort(reverse=True)
boxs.sort(reverse=True)

result = 0
if crains[0] < boxs[0]:
    result = -1
else:
    while boxs:
        result += 1

        for c in crains:
            for i in range(len(boxs)):
                if c >= boxs[i]:
                    boxs.pop(i)
                    break
            
print(result)