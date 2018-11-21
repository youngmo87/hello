
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
    

class Hand(Card):
    def __init__(self):
        self.cardtotal
    
    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10' 
        
        elif 'A' in card[1]:
            self.eachvalue = '11'
        
        else:
            self.eachvalue = card[1]

        return self.eachvalue           

class Scoring(Game):
    def __innit__(self, dealervalue, playervalue):
        self.dealersum=sum(dealervalue)
        self.playersum=sum(playervalue)

    def inputmsg(self, dealerchoice):
        msg= input("딜러의 첫번째 카드는 {}입니다. {}의 현재카드는 {} 입니다. \n 카드를 더 받으시겠습니까?.그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(dealer.pick,player.name,player.deck))
        if msg == 'H':

class Player(Game):
    hand=[]
    value=[]
    def __init__(self):
        self.firstcard=self.cardtotal.pop(0)
        self.hand.append(self.firstcard)
        self.valueassign(self.firstcard)
        self.value.append(self.eachvalue)
    
    def cardpick(self):
        self.addcard=self.cardtotal.pop(0)
        self.hand.append(self.addcard)
        self.valueassign(self.addcard)
        self.value.append(self.eachvalue)


class Dealer(Game):
    hand=[]
    value=[]
    def __init__(self):
        self.firstcard=self.cardtotal.pop(0)
        self.hand.append(self.firstcard)
        self.valueassign(self.firstcard)
        self.value.append(self.eachvalue)
    
    def cardpick(self):
        self.addcard=self.cardtotal.pop(0)
        self.hand.append(self.addcard)
        self.valueassign(self.addcard)
        self.value.append(self.eachvalue)
        

    
    
card1=Card()
deck1=Deck()
player1=Player()
dealer1=Dealer()
print(deck1.cardtotal)
print(len(deck1.cardtotal))
print(player1.deck)
print(player1.eachvalue)
print(player1.value)
print(dealer1.deck)
print(dealer1.eachvalue)
print(dealer1.value)
player1.cardpick()
dealer1.cardpick()
print(player1.deck)
print(player1.eachvalue)
print(player1.value)
print(dealer1.deck)
print(dealer1.eachvalue)
print(dealer1.value)

card1.cardtotal=0
deck1.cardtotal=0
player1.deck=0
player1.eachvalue=0
player1.value=0
dealer1.deck=0
dealer1.eachvalue=0
dealer1.value=0
a=[1,2]
b=sum(a)
print(b)
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