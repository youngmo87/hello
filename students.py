# with open("student.csv", "w", encoding='utf8') as file:
#     file.write ("이름,성별,나이,성적\n김일수,남,23,90\n이이수,여,24,95\n박삼수,여,30,85\n현사수,남,35,50\n부오수,남,15,70\n고육수,여,27,60\n양칠수,남,25,55\n남팔수,남,22,88\n오구수,여,45,99\n유영수,남,11,40\n")

# file=open("student.csv", "r")


# with open("student.csv", "r", encoding='utf8') as file:

class Student:
    def __init__(self, name, sex, age, score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
        
        # if score >=90:
        #     self.score=self.score+"(A학점)"
        # elif score >=80:
        #     self.score=score("B학점")
        # elif score >=70:
        #     self.score="C학점"
        # else:
        #     self.score="D학점"
        
    
    def __str__(self):
        return "{}:{}:{}:{}".format(self.name[0]+"**", self.sex, self.age, self.score)

class Point(Student)
    def __init__(self, name, sex, age, grade):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = score
         if score >=90:
            self.score=self.score+"(A학점)"
        elif score >=80:
            self.score=score("B학점")
        elif score >=70:
            self.score="C학점"
        else:
            self.score="D학점"
    def __str__(self):
        return "{}:{}:{}:{}".format(self.name[0]+"**", self.sex, self.age, self.score)

students = [
    Student("김일수", "남", 23, 90),
    Student("이이수", "여", 24, 95),
    Student("박삼수", "여", 30, 85),
    Student("현사수", "남", 35, 50),
    Student("부오수", "남", 15, 70),
    Student("고육수", "여", 27, 60),
    Student("양칠수", "남", 25, 55),
    Student("남팔수", "남", 22, 88),
    Student("오구수", "여", 45, 99),
    Student("유영수", "남", 11, 40)
    ]

# for i in range(0,10):
#     t=student[i]

def print_students():
    print("--------------------")
    for s in students:
        print(s)


# sort_students = sorted(students, key = lambda stu: stu.score)
# print_students()

# students.sort(key = lambda stu: stu.score)
# print_students()

students.sort(key = lambda stu: stu.score, reverse=True)
print_students()



