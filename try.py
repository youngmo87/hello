i, sum = 0, 0
while (i >= 0):
    i += 1
    sum += i # sum=3
    if (i == 100):
        print("End!!", sum)
        break

i, sum = 0, 0
while (i >= 0):
    i += 1
    if (i%2 == 0):
      continue
    sum += i 
    if (i == 99):
        print("End!!", sum)
        break

i, sum = 0, 0
while (i >= 0):
    i +=2
    sum +=i
    if (i == 100):
        print("End!!", sum)
        break

####짝수
i, sum = 0, 0
while (i <= 100):
    i +=2
    sum +=i
    if (i == 100):
        print("End!!", sum)
        break

##홀수
i, sum = 1, 0
while (i <= 100):
    sum +=i
    i +=2
    if (i == 101):
        print("End!!", sum)
        break

##for 
sum=0
for i in ragne(1,101):
    sum=sum+i


i, sum = 0, 0
while (i >= 1):
    sum +=i
    i +=2
    if (i == 102):
        print("End!!", sum)
        break

i, sum = 0, 0
while (i >= 0):
    sum +=i
    i +=2
    if (i == 102):
        print("End!!", sum)
        break