def to_int(s):
    if type(s) == str:
        return int(s)
    else:
        return s

class Quadro:
    def __init__(self):
        self.name="사각형과제"
    
    def start(self):
        input("사각형의 형태는? 다음보기중 선택하세요 \n(a). 평행사변형 \n(b). 직사각형 \n(c). 정사각형\n>>")      

    def cal(self, a, b):
        return int(a) * int(b)

quadro=Quadro()

class Parallel(Quadro):
    def start1(self):
        input("평행사변형 넓이는 밑변 x 높이 입니다. 밑변과 높이 사이는 comma로 구분해주세요>>")

parallel=Parallel()

class Rect(Parallel):
    def start2(self):
        input("직사각형 넓이는 가로 x 세로 입니다. 가로와 세로 사이는 comma로 구분해주세요>>")

rect=Rect()


class Square(Rect):
    def start3(self):
        input("정사각형 넓이는 한변의 제곱 입니다. 한변의 길이만 입력해 주세요>>")

  
    def cal(self, a):
        return int(a) * int(a)

square=Square()

outmsg = "답은 {}"

while True:
    quadro_type=input("사각형의 형태는? 다음보기중 선택하세요 \n(a). 평행사변형 \n(b). 직사각형 \n(c). 정사각형\n>>")      
    r1=input("평행사변형 넓이는 밑변 x 높이 입니다. 밑변과 높이 사이는 comma로 구분해주세요>>")
    r2=input("직사각형 넓이는 가로 x 세로 입니다. 가로와 세로 사이는 comma로 구분해주세요>>")
    r3=input("정사각형 넓이는 한변의 제곱 입니다. 한변의 길이만 입력해 주세요>>")

    if quadro_type == 'a':
        parallel.start1()
        x,y=r1.split(',')
        result=cal(x,y)
        print(outmsg.format(result))
        
    elif quadro_type == 'b':
        rect.start2()
        x,y=r2.split(',')
        result=cal(x,y)
        print(outmsg.format(result))

    else: 
        square.start3()
        x,y=r3.split(',')
        result=cal(x,y)
        print(outmsg.format(result))

        


#x,y=split(',')