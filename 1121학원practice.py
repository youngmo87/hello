import random

Class=[]
playerinit=['김일수','김이수', '김삼수','김사수','김오수','김육수','김칠수']
# a=7
# for i in range(1,int(a)+1):
#     playerinit.append('player' + str(i))

# for i in range(1,int(a)+1):
#     playerinit.append('player' + str(i))


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
    
class Game(Card):
    print("게임클래스가생성됨")    
    def __init__(self):
        self.cardtotal
        for i in playerinit:
            i=Player(i)
            Class.append(i)
    
    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10' 
        
        elif 'A' in card[1]:
            self.eachvalue = '11'
        
        else:
            self.eachvalue = card[1]

        return self.eachvalue   
    
    def cardpick(self):
        self.firstcard=self.cardtotal.pop(0)
        self.hand.append(self.firstcard)
        self.valueassign(self.firstcard)
        self.value.append(self.eachvalue)

    def additionalpick(self):       
        self.additionalcard=self.cardtotal.pop(0)
        self.hand.append(self.additionalcard)
        self.valueassign(self.additionalcard)
        self.value.append(self.eachvalue)

class Player(Game):
    def __init__(self,x):
        print("{}가 플레이합니다".format(x))
        self.hand=[]
        self.value=[]

    def Playerplay(self):
        for i in Class:
            i.additionalpick()

class Dealer(Game):
    def __init__(self):
        self.hand=[]
        self.value=[]

    def Dealerplay(self):
        self.cardpick()
        

    

    # # def eachpick(self):    
        
        # self.addcard=self.cardtotal.pop(0)
        # self.deck.append(self.addcard)
        # self.valueassign(self.addcard)
        # self.value.append(self.eachvalue)




card=Card()
try1=Game()

for i in Class:
    i.cardpick()


print(Class[2].firstcard)
print(Class[2].eachvalue)
print(Class[2].value)
print(Class[2].deck)
print(Class[3].firstcard)
print(Class[3].eachvalue)
print(Class[3].value)
print(Class[3].deck)

# player1.cardpick()
# dealer1.cardpick()
# print(player1.deck)
# print(player1.eachvalue)
# print(player1.value)
# print(dealer1.deck)
# print(dealer1.eachvalue)
# print(dealer1.value)