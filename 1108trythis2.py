def mul(a,b):
    return a * b

start1 = input("사각형의 형태는? 다음보기중 선택하세요 (a). 사격형 (b). 직사각형 (c). 평행사변형>>")

if 'b' in start1:
    start3 = input("직사각형 넓이는 가로 x 세로 입니다. 가로와 세로 사이는 comma로 구분해주세요>>")
    cala = start3.split(',')
    outmsg = "답은 {}"
    a=int(cala[0])
    b=int(cala[2])
    print(outmsg.format(mul(a,b)))
    
elif 'c' in start1:
    start4 = input("평행사변형 넓이는 밑변 x 높이 입니다. 밑변과 높이 사이는 comma로 구분해주세요>>")
    calb = start4.split(',')
    outmsg = "답은 {}"
    a=int(calb[0])
    b=int(calb[2])
    print(outmsg.format(mul(a,b)))
