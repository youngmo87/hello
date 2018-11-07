# 1부터 10까지의 소수 합 실패!!!
i, sum = 0, 0
while (i >= 0):
	i += 1
	a1 = i / 2
	b1 = i / 3 
	c1 = i / 5 
	d1 = i / 7
	if (a1 != 1 or b1 != 1 or c1 != 1 or d1 != 1):
		continue

# 10부터 100까지의 소수 합
i, sum = 0, 0
while (i >= 0):
	i +=1
	a = i % 2 
	b = i % 3 
	c = i % 5 
	d = i % 7 
	if (a==0 or b==0 or c==0 or d==0):
		continue
	
	sum += i 
	if (i == 97):
		print("End!!", sum-1) #1을 제외함
		break
p=sum-1
q=2+3+5+7 #어떻게하면 효율적일까?ㅋㅋㅋ

print("일의 자리 소수합 + 10에서 100사이에 소수합은", p+q)
