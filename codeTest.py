num = int(input())

def prime(i) : # 소수 확인
    if i == num or i % 2 != 0 or i == 2 :
        return True
    else :
        return False

def main() : # 인수 확인
    for i in range(2, num + 1) :
        if num % i == 0 and prime(i):
            return i

while num > 1 :
    result = main()
    print(result)
    num //= result

