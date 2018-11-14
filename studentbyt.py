g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()
from functools import reduce
from studentclass import Student


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
