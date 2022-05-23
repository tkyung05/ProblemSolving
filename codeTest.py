m = int(input())
n = int(input())

data = []
primeCh = True
sum = 0
min = 0

def FindByPrime(num) :
   global sum
   global primeCh
   global data

   if num == 1 :
      return

   bug = False

   for i in range(2, num) :
      if num % i == 0 :
         bug = True
   if not bug:
      data.append(num)
      sum += num
      primeCh = False


# main
for num in range(m, n + 1) :
   if num != 2 :
      FindByPrime(num)
   else :
      data.append(num)
      sum += num
      primeCh = False




if primeCh :
   data.append(-1)

data.sort()
min = data[0]

if not primeCh :
   print(sum)
print(min)
