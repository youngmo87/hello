g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()
from functools import reduce

class Student:
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        # if self.score == 100:
        #     self.grade = 'A+'
        # else:
        #     self.grade = g_grades[ self.score // 10 - 5 ]
    
        if self.score >=90:
            self.grade="(A학점)"
        elif self.score >=80:
            self.grade="(B학점)"
        elif self.score >=70:
            self.grade="(C학점)"
        else:
            self.grade="(D학점)"


students=[]
with open('student.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append(Student(line))

students.sort(key = lambda stu: stu.score, reverse = True)
m = map(lambda stu: stu.make_grade(), students)
list(m) #map은 list라는 용어를 써야 출력된다. 그래서 위에 m=map라고 정의 했다. 



print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

#type(x) == int ? A : B true면 A false면 B
t = reduce(lambda x,y:(x if type(x) == int else x.score)+y.score,students)

# reduce에서 위의 식같은경우로 나타내지 못할경우는 아래와 같은 식도 적용된다.
# def sumfn(x,y):
#     if type(x) == int:
#         return x+y.score
#     else:
#         return x.score + y.score
# total=reduce(sumfn, students)

print("총점수>>", t)
print("평균은>>", t/len(students))

print("---------------------------")
for s in students:
    if s.score >= t/len(students):
        print(s)

#nodemon --exec python 파일명 파이썬에서 실행하는법 노드몬 끝내는 단축키는 ctrl+c
