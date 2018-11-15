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

class Dealer(Card):
    def __init__(self):
        self.start = cardtotal.pop()
        if 'J' or 'Q' or 'K' or 'F' in self.start:
            self.start = 10
        elif 'A' in self.start:
            self.start = 11
        else:
            self.start = int(self.start[1])       
      
    def cardpick(self):
        if 'J' or 'Q' or 'K' or 'F' in self.choice:
            self.choice = 10
        elif 'A' in self.choice:
            self.choice = 11
        else:
            self.choice = int(self.choice[1])       
      
        self.choice = cardtotal.pop()
    def value(self):
            self.value = self.start + self.choice


class Player(Card):
    def __init__(self):
        self.start = cardtotal.pop()
        if 'J' or 'Q' or 'K' or 'F' in self.start:
            self.start = 10
        elif 'A' in self.start:
            self.start = 11
        else:
            self.start = int(self.start[1])       
      
    def cardpick(self):
        self.choice = cardtotal.pop()
        if 'J' or 'Q' or 'K' or 'F' in self.choice:
            self.choice = 10
        elif 'A' in self.choice:
            self.choice = 11
        else:
            self.choice = int(self.choice[1])       
      
    def value(self):
        self.value = self.start + self.choice
        
    #     print(value)
    # def value(self):

# class CardCalc(Card):
#     def __init_(self):
        
    
Card()
Player()
Dealer()
try1=Card()
player1=Player()
dealer=Dealer()
dealer.cardpick()
dealer.value()
print(dealer.value)
# try1.value()
# print(choice)

# try1.value()




# choice1=cardtotal.pop(0)

# if 'A' in choice1: 
#     choice1 = choice1[0] + '11' 
# if 'J' in choice1: 
#     choice1 = choice1[0] + '10' 
# if 'Q' in choice1: 
#     choice1 = choice1[0] + '10' 
# if 'K' in choice1: 
#     choice1 = choice1[0] + '10' 
# if 'F' in choice1: 
#     choice1 = choice1[0] + '10' 


# choice2=cardtotal.pop(0)

# if 'A' in choice2: 
#     choice2 = choice2[0] + '11' 
# if 'J' in choice2: 
#     choice2 = choice2[0] + '10' 
# if 'Q' in choice2: 
#     choice2 = choice2[0] + '10' 
# if 'K' in choice2: 
#     choice2 = choice2[0] + '10' 
# if 'F' in choice2: 
#     choice2 = choice2[0] + '10' 

# if len(choice1)<=2:
#     a = int(choice1[1])
# else:
#     a=10

# if len(choice2)<=2:
#     b = int(choice2[1])
# else:
#     b=10

# cardvalue = a + b
# print(cardvalue)



# tyrthis=ValueSum()

