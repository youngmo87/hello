import random

cardsort = ['S','C','H','D']
cardnum = [*'23456789FAJQK']

sort=len(cardsort)
num=len(cardnum)

cardtotal=[]

for i in range(sort):
    for k in range(num):
        cardtotal.append(cardsort[i]+cardnum[k])

if cardtotal[-1]=='F':
    cardtotal[-1]='10'
if cardtotal[-1]=='J':
    cardtotal[-1]='10'
if cardtotal[-1]=='K':
    cardtotal[-1]='10'
if cardtotal[-1]=='Q':
    cardtotal[-1]='10'
if cardtotal[-1]=='A':
    cardtotal[-1]='10'

random.shuffle(cardtotal)
choice1=cardtotal.pop(1)
choice2=cardtotal.pop(2)

class ValueSum:
    def __init__(self):
        self.value = int(choice1[-1]) + int(choice2[-1])


tyrthis=ValueSum()
