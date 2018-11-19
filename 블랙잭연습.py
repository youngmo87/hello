import random
class Card:
    cardtotal=[]
    def __init__(self):
        self.cardsort = ['D','C','S','H']
        self.cardnum = ['2','3','4','5','6','7','8','9','10','10','10','10','11']
        self.a=len(self.cardsort)
        self.b=len(self.cardnum)
        self.cardmix(self.a, self.b)

    def cardmix(self, cardsort, cardnum):
        for i in range(cardsort):
            for k in range(cardnum):
                self.cardtotal.append(self.cardsort[i]+self.cardnum[k])

try2=Card()
print(try2.cardtotal)


print(try1.mkdir)
print(try1.cardsort)
print(try1.cardtotal)


pick = ['S','S9', 'S1', 'S3']
'S' in pick
if pick[1] == 'J' or 'Q' or 'K' or 'F':
    print('5')
elif pick[1] == 'A':
    print('10')
else:
    print(int(pick[1]))    

print(value)

numbers = ['one', 'two', 'three', 'four', 'five']
    
for n in numbers:
    print(n)