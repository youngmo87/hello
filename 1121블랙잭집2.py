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
        self.name=[]
        self.cardtotal
        for i in playerinit:
            i=Player(i)
            Class.append(i)
    
    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = 10 
        
        elif 'A' in card[1]:
            self.eachvalue = 11
        
        else:
            self.eachvalue = int(card[1])

        return self.eachvalue   
    
    def cardpick(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.valueassign(self.carddraw)
        self.value.append(self.eachvalue)
        self.results(self.name, self.hand, self.value)

    def playerpick(self):
        for i in Class:
            i.cardpick(self.name)
        dealer.Dealerplay()
 
    def additionalpick(self):
        for i in Class:
            i.cardpick(self.name)     
        dealer.Dealerplay()
    
    def results(self, name, hand, value):
        return Result(name, hand, sum(value))
     
class Result():
    def __init__(self, name, hand, value):
        self.name=name
        self.hand=hand
        self.value=value
        print("결과클래스")
    
    # def dealerasking(self):
    #     for i in Class:
    #         msg=input("{}님 카드를 더 받으시겠습니까? 현재카드는 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.sum,self.hand))
    #         if msg == 'S':
    #             return 
    #         if msg == 'H': 
    #             return   

            
class Player(Game):
    def __init__(self,i):
        self.name=i
        self.hand=[]
        self.value=[]
        print("{}가 플레이합니다".format(i))
    
    def Playerplay(self):
        self.playerpick()

class Dealer(Game):
    def __init__(self):
        self.name='딜러임'
        self.hand=[]
        self.value=[]
        
    def Dealerplay(self):
        self.cardpick(self.name)
           
   
card=Card()
dealer=Dealer()
try1=Game()
try1.playerpick()

# print(try1.cardtotal)
# print(Class[2].hand)
# print(Class[2].value)
# print(Class[3].hand)
# print(Class[3].value)
# print(dealer.hand)
# print(dealer.value)
try1.additionalpick()
# print(try1.cardtotal)
# print(Class[2].hand)
# print(Class[2].value)
# print(Class[3].hand)
# print(Class[3].value)
# print(dealer.hand)
# print(dealer.value)


