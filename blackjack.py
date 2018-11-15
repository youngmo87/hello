import random


cardsort = ['S','C','H','D']
cardnum = [*'23456789FAJQK']

sort=len(cardsort)
num=len(cardnum)

cardtotal=[]
class Card:
    def __init__(self):
        for i in range(sort):
            for k in range(num):
                cardtotal.append(cardsort[i]+cardnum[k])
                random.shuffle(cardtotal)    

    def cardpick1(self, pick):
        self.pick = cardtotal.pop(0)
    
    def cardpick2(self, pick):
        self.pick = 


class CardPick


class CardCalc(Card):




choice1=cardtotal.pop(0)

if 'A' in choice1: 
    choice1 = choice1[0] + '11' 
if 'J' in choice1: 
    choice1 = choice1[0] + '10' 
if 'Q' in choice1: 
    choice1 = choice1[0] + '10' 
if 'K' in choice1: 
    choice1 = choice1[0] + '10' 
if 'F' in choice1: 
    choice1 = choice1[0] + '10' 


choice2=cardtotal.pop(0)

if 'A' in choice2: 
    choice2 = choice2[0] + '11' 
if 'J' in choice2: 
    choice2 = choice2[0] + '10' 
if 'Q' in choice2: 
    choice2 = choice2[0] + '10' 
if 'K' in choice2: 
    choice2 = choice2[0] + '10' 
if 'F' in choice2: 
    choice2 = choice2[0] + '10' 

if len(choice1)<=2:
    a = int(choice1[1])
else:
    a=10

if len(choice2)<=2:
    b = int(choice2[1])
else:
    b=10

cardvalue = a + b
print(cardvalue)



tyrthis=ValueSum()

