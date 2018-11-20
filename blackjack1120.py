
import random
class Card:
    cardtotal=[]
    def __init__(self):
        self.cardsort = ['S','C','H','D']
        self.cardnum = ['2','3','4','5','6','7','8','9','F','A','J','Q','K']
        self.card =[]
        self.cardsready(self.cardsort, self.cardnum)

    def cardsready(self, a, b):
        for i in a:
            for k in b:
                self.card=i+k
                self.cardtotal.append(self.card) 

        return random.shuffle(self.cardtotal)   
    

class Deck(Card):
    deck=[]
    eachvalue=[]
    def __init__(self):
        self.cardtotal
    
    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = 10 
        
        elif 'A' in card[1]:
            self.eachvalue = 11
        
        else:
            self.eachvalue = int(card[1])

        return self.eachvalue           

        # self.valueassign(self.deck)
        # self.valuelist=self.value.append(self.eachvalue)    

pick=[]



class Player(Deck):
    def __init__(self):
        self.deck=self.cardtotal.pop(0)
        self.valueassign(self.deck)
        
    # def cardpick(self):    
    #     self.valueassign(self.deck)

card1=Card()
deck1=Deck()
player1=Player()
print(card1.cardtotal)
print(deck1.cardtotal)
print(player1.deck)
# print(player1.value)
print(deck1.eachvalue)
print(player1.eachvalue)
card1.cardtotal=0
deck1.shape=0
deck1.deck=0
deck1.cardtotal=0    
player1.deck=0

print(cardtotal)
    # def cardvalue(self):
    #     valueassign=cardtotal.pop(0)
    
    #  


dealerdeck=[]
class Dealer(Card):
    def __init__(self):
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
