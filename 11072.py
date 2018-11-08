def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    # if b == 0
    #     return 
    return a / b

cal = input("Input(usage: 숫자 연산자 숫자)>>")
cals = cal.split(' ')
outmsg="답은 {}"

a=int(cals[0])
b=int(cals[2])

if '+' in cals:
    print(outmsg.format(plus(a,b)))    
elif '-' in cals:
    print(outmsg.format(minus(a,b)))
elif '*' in cals:
    print(outmsg.format(mul(a,b)))
elif '/' in cals:
    print(outmsg.format(div(a,b)))
