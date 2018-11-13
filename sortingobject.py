class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]

def print_students():
    print("--------------------")
    for s in students:
        print(s)

print_students()