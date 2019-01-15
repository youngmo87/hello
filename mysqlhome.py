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


# import sqlite3

import pymysql
import random


name=[]
fam_names = [*'김이박최강고윤엄한배성백전황서청방지마피']
first_names = [*'건성현육정민현주희진영래주동헤도모영진선재현호시우인성마무병별솔하라']
a=fam_names
b=first_names
for i in a:
    for k in b:
        for j in b:
            name.append(i+k+j)
random.shuffle(name)
nameready=name[0:1000]

tel=[]
first =['010']
num=[*'0123456789']
second = []
third = []
for i in num:
    for k in num:
        for j in num:
            for q in num:
                second.append(i+k+j+q)
                third.append(i+k+j+q)

for i in range(1000):
    a=random.choice(second)
    b=random.choice(third)
    tel.append('010-'+a+'-'+b)


email=[]
alphabet=[*'abcdefghijklmnopqrstuvwxyz']
for i in range(1000):
    a=random.sample(alphabet, 6)
    b=random.sample(num, 4)
    c="".join(a)
    d="".join(b)
    email.append(c+d+'@gmail.com')



birth=[]
year=[]
day=[]

yeardata=[*'0123456789']
monthdata=['01','02','03','04','05','06','07','08','09','10','11','12']
daydata=[*'0123456789']

for i in yeardata:
    for j in yeardata:
        a=year.append(i+j) 

for i in range(1000):
    dd=random.choice(daydata)
    if dd in ['1','2']:
        for k in daydata:
            day.append(dd + k)

    elif dd == '3':
        for k in ['0','1']:
            day.append(dd + k)

    elif dd == '0':
        for k in daydata:
            day.append(dd + k)
            
for i in range(1000):
    birth.append(random.choice(year) + random.choice(monthdata) + random.choice(day))


addrdataset=[]
addr=['서울','경기','강원','충북','충남','전북','전남','경북','경남','제주','부산','인천','광주','대구','울산']
for i in range(1000):
    addrdata=random.choice(addr)
    addrdataset.append(addrdata)


finaldata=[]
for i in range(1000):
    dataset=tuple([nameready[i], addrdataset[i], tel[i], email[i], birth[i]])
    finaldata.append(dataset)

conn = pymysql.connect(host='localhost', user='dooo', password='dooo!', port=3306, db='dooodb', charset='utf8')
curs = conn.cursor()


sql = """insert into info(name, addr, tel, email, birth)
         values (%s, %s, %s, %s, %s)"""

curs.executemany(sql, finaldata)
conn.commit()



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
