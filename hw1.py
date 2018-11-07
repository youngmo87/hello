sum=0
for i in range (2, 101):
    if (2 <= j < 100):
        if (j < i):
            a = (i % j)
            if (a == 0 ):    
                continue     
            sum += i 
            if (i == 101):
                print("END", sum)
                break