# import sqlite3
 
# conn = sqlite3.connect("test.db")
 
# with conn:
#     cur = conn.cursor()
#     sql = "select * from Student where id=? or name=?"
#     rows = cur.execute(sql, (3, '홍길동'))
#     # rows = cur.fetchall()
            
#     for row in rows:
#         print(row)

# import sqlite3

# conn = sqlite3.connect("test.db")

# with conn:
#     cur = conn.cursor()
#     sql = "insert into Student(name, mobile) values(?,?)"
#     cur.execute(sql, ('김삼순', None))

# #     conn.commit()

# import sqlite3
# import random

# name=[]
# fam_names = [*'김이박최강고윤엄한배성백전황서청방지마피']
# first_names = [*'건성현육정민현주희진영래주동헤도모영진선재현호시우인성마무병별솔하라']
# a=fam_names
# b=first_names
# for i in a:
#     for k in b:
#         for j in b:
#             name.append(i+k+j)
# random.shuffle(name)
# nameready=name[0:100]

# data=[]
# def insertready(a):
#     for i in enumerate(a):
#         data.append(i)        
# insertready(nameready)
# print(data)
# data=tuple(data)
# print(data)

# conn = sqlite3.connect("test.db")

# with conn:
#     cur = conn.cursor()
#     sql = "insert into Student(id, name) values(?,?)"
#     cur.executemany(sql, data)

#     conn.commit()


class Test:
    def __init__(self):
        self.__color = "blue"
    @property
    def color(self):
        return self.__color

    # @color.setter
    # def color(self,clr):
    #     self.__color = clr



t = Test()
t.color = "Red"

print(t.color)


