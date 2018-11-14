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
