import random


cardsort = ['S','C','H','D']
cardnum = [*'23456789FJQKA']

sort=len(cardsort)
num=len(cardnum)

cardtotal=[]
class Card:
    def __init__(self):
        for i in range(sort):
            for k in range(num):
                cardtotal.append(cardsort[i]+cardnum[k])
                random.shuffle(cardtotal)    
    
    def cardpick(self):
        self.pick=cardtotal.pop()
        self.pick=self.deck.extend([self.pick])
        

class Dealer(Card):
    def __init__(self):
        self.deck=[]
        self.pick2=cardtotal.pop()
        self.pick2=self.deck.extend([self.pick2])
        self.sum=0

    def scoring(self): 
        self.sum=0
        for i in range(len(self.deck)):
            if type(self.deck[i]) == int: 
                self.deck[i]=self.deck[i]
    
            elif 'A' in self.deck[i][1]:
                self.deck[i] = 11

            elif self.deck[i][1] in ['J','Q','K','F']:
                self.deck[i] = 10
            
            else:
                self.deck[i] = int(self.deck[i][1])
            
            self.sum = self.sum + self.deck[i]

try1=Card()
dealer=Dealer()
dealer.cardpick()
print(dealer.pick)
print(dealer.deck)
dealer.scoring()
print(dealer.deck)
print(dealer.sum)
dealer.cardpick()
dealer.scoring()
print(dealer.deck)
print(dealer.sum)
dealer.cardpick()
dealer.scoring()
print(dealer.deck)
print(dealer.sum)

