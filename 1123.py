# class Result:
#     def __init__(self, name, idnum):
#         print("클래스가 생성되었습니다.")
#         self.name =name
#         self.idnum=idnum
#         self.callclass(self.name, self.idnum)
    
#     def callclass(self, name, idnum):
#         self.name=name
#         self.idnum=idnum
#         print("{}님 아이디는{}가 생성되었습니다.".format(self.name,self.idnum))


# class Name:
#     def __init__(self, name, idnum):
#         self.name=name
#         self.id=idnum
#         Result(self.name, self.id)


# player1=Name('김일수','1번')
# player2=Name('김이수','2번')
# player3=Name('김삼수','3번')

# print(id(player1.name))
# print(id(player2.name))
# print(id(player3.name))


def write_file():
    with open("a.csv", "a") as file:
        file.write("이름,성별,나이\n")
        file.write("김일수,남,14\n")
        file.write("김이수,남,24")

def write_file2(seq):
    with open("a.csv", "w") as file:
        file.writelines(seq)

def read_file():
    with open("a.csv", "r") as file:
        for line in file:
            print("line>>", line)

def write_file3(l):
        with open("a.csv", "wa") as file:
                for i in l:
                        file.write(i)
                        file.write("\n")


write_file()
read_file()

lst = ['김삼수\t여\t33', '김사수\t남\t41', '김오수\t여\t77']
write_file3(lst)