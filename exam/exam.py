# import sqlite3


# conn = sqlite3.connect('exam.db')


# with conn:
#     cur = conn.cursor()
#     condition1 = update exam set  = substr(mobile, 5) where id > 0; 


# insert into Exam(id, name, grade, addr)



students=[]
class Student:
    def __init__(self, line):
        name, gender, age, grade, addr = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.grade = int(grade)
        self.addr = addr 
    # def __str__(self):
    #     return "{}\{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade, self.addr)

class Point(Student):
    def __init__(self, name, gender, age, grade, addr):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.addr = addr

        if grade >=90:
            self.score=self.score+"(A학점)"
        
        elif grade >=80:
            self.grade=("B학점")
        
        elif grade >=70:
            self.score="C학점"
        
        else:
            self.grade ="D학점"
    
    def __str__(self):
        return "{}:{}:{}:{}".format(self.name[0]+"**", self.sex, self.age, grade, addr)

with open("students.csv","r", encoding='utf8')as file:
    for i, line in enumerate(file):
        if i == 0:continue
        students.append(Student(line))


for i in students:
    Point(i)
    
print(students)
