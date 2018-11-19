import random



class Card:
    cardtotal=[]
    def __init__(self):
        self.cardsort = ['S','C','H','D']
        self.cardnum = ['2','3','4','5','6','7','8','9','F','A','J','Q','K']
        self.sort=len(self.cardsort)
        self.num=len(self.cardnum)

    def calc(self):
        for i in range(self.sort):
            for k in range(self.num):
                self.cardtotal.append(self.cardsort[i]+self.cardnum[k])
card1=Card()
card1.calc()


class Deck:
    def__init__(self):
    self.deck=[]
    
card1.cardtotal=0

print(cardtotal)
    # def cardvalue(self):
    #     valueassign=cardtotal.pop(0)
    
    #     if 'J','Q','K','F' in valueassign[1]: 
    #         self.value = valueassign[0] + '10' 
        
    #     elif 'A' in valueassign:
    #         self.value = valueassign[0] + '11' 
        
    #     else:
    #         self.value = valluassign[1] 
        
        # if len(self.value)<=2:
        #     self.value = int(valluassign[1])
        # else:
        #     self.value=10


dealerdeck=[]
class Dealer(Card):
    def __init__(self):
        cardtotal.pop(0)
        self.deck = dealerdeck.append(cardtotal.pop())
    
    def start(self):
        self.deck = dealerdeck.append(cardtotal.pop())

    def calc(self):
        self.total = a + b
        
playerdeck=[]   
class Player(Card):
    def __init__(self):
        cardtotal.pop()
        self.deck = playerdeck.append(cardtotal.pop())
    
    def start(self):
        self.deck = playerdeck.append(cardtotal.pop())



Card()
play=Player()
deal=Dealer()
deal.start()
print(dealerdeck)

play.start()
print(playerdeck)

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
