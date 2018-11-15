import random

cardsort = ['S','C','H','D']
cardnum = [*'23456789FAJQK']

sort=len(cardsort)
num=len(cardnum)

cardtotal=[]

for i in range(sort):
    for k in range(num):
        cardtotal.append(cardsort[i]+cardnum[k])

# random.shuffle(cardtotal)

choice1=cardtotal.pop(16)
if choice1[1] == 'A':
    choice1='10'

if choice1[1] == 'F':
    choice1='10'
if choice1[1] == 'J':
    choice1='10'
if choice1[1] == 'Q':
    choice1='10'
if choice1[1] == 'K':
    choice1='10'

choice2=cardtotal.pop(1)
if choice2[1] == 'A':
    choice2='10'
if choice2[1] == 'F':
    choice2='10'
if choice2[1] == 'J':
    choice2='10'
if choice2[1] == 'Q':
    choice2='10'
if choice2[1] == 'K':
    choice2='10'


if len(choice1)==2:
    a= int(choice1[1])
if len(choice2)==2:
    b =int(choice2[1])

else:
    a=int(10)
    b=int(10)

cardvalue = a + b


print(cardvalue)

# class ValueSum:
#     def __init__(self):
#         self.value = int(choice1[-1]) + int(choice2[-1])


# tyrthis=ValueSum()

#브랜치테스트