
class Square:
    def __init__(self):
        self.name = "대빵"
    
class Parall(Square):
    def __init__(self):
        print ("평행사변형")
        print ("평행사변형 넓이를 구하는 방법은")
    def baseheight(self, a, b):
        self.area = a * b
        print("밑변 {} 곱하기 높이 {}는".format(a, b), self.area) 

           
class Rectang(Parall):
    def __init__(self):
        print ("직사각형")
        print ("직사각형 넓이를 구하는 방법은")
    def lonlat(self, a, b):
        self.area = a * b
        print("가로 {} 곱하기 세로 {}는".format(a, b), self.area)
    

square1 = Square()
square2 = Parall()
square3 = Rectang()
