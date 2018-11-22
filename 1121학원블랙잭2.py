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
        self.name=i
    
    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10'
        
        elif 'A' in card[1]:
            self.eachvalue = '11'
        
        else:
            self.eachvalue = card[1]

        return self.eachvalue   
    
    def cardpick1(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.valueassign(self.carddraw)
        self.value.append(self.eachvalue)
        # self.scoring(self.name, self.hand, self.value)
    
    def cardpick2(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.valueassign(self.carddraw)
        self.value.append(self.eachvalue)
        self.scoring(self.name, self.hand, self.value)

    def playerpick(self):
        for i in Class:
            i.cardpick1(self.name)
        dealer.Dealerplay()
 
    def additionalpick(self):
        for i in Class:
            i.cardpick2(self.name)     
        dealer.Dealerplay()
        
    
    def scoring(self, name, hand, value):
        return Scoring(name, hand, value)

    def dealerasking(self):
        for i in Class:
            msg=input("{}님 카드를 더 받으시겠습니까? 현재카드는 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.name,self.hand))
            if msg == 'S':
                Class.pop(i)
                if '11' in self.value:
                    self.value.count('11')
                    question=input("에이스가 {} 개 있네요. 무엇으로 하시겠습니까? 1개면 원하는 숫자를\n 두개이상이면 '1' 또는 '11'을 차례대로 입력해주세요!\n 'AA'일 경우 '11,11' 혹은 '1,1 (콤마로구분)".format(self.value.count('11')))
                    acechoice=question.split(',')
                    for i in acechoice:
                        choiceassign=[]
                        choiceassign=choiceassign.append(i)
                        if '11' in choiceassign:
                            self.finalresult=self.sum - 10*int(choiceassign.count('11'))
                        else:
                            self.finalresult=self.sum
                else:
                    self.finalresult=self.sum

                return self.calc(self.sum)
                
            if msg == 'H': 
                return self.cardpick2(self.name)
    
    def calc(self, sum):
        self.finalresult=[]
        self.sum=sum
        
        if  self.sum < 21:
            for i in self.finalresult:
                min(21-i)
 
        elif self.sum > 21:
            print("운이없네요......")
        elif self.finalresult == 21:
            print("블랙잭입니다")



class Scoring(Game):
    def __init__(self, name, hand, value):
        self.sum=0
        self.name=name
        self.hand=hand
        self.value=value
        for i in self.value:
            self.sum+=int(i)
        print("점수클래스")
        # self.dealerlogic(self.value, self.sum)

    def d_pickforace(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.d_valueforace(self.carddraw)
        self.value.append(self.eachvalue)
        self.scoring(self.name, self.hand, self.value)
        self.dealerasking()
    
    def d_valueforace(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10'
        elif 'A' in card[1]:
            self.eachvalue = '11'
        else:
            self.eachvalue = card[1]
        return self.eachvalue  

    def dealerlogic(self, value, valuesum):
        while '11' not in self.value:
            if valuesum >= 17:
                print("가가가",self.name)
                return  self.calc(self.sum)
            
            elif valuesum < 17:
                print("나나나",self.name)
                return self.cardpick2(self.name)
                  
        while '11' in self.value:   
            if valuesum == 21:
                print("다다다",self.name)
                return self.calc(self.sum)                  
            
            elif valuesum < 17:
                print("라라라",self.name)
                return self.cardpick2(self.name)
            
            elif valuesum > 21:
                self.value.remove('11')
                self.value.append('1')

                self.sum=self.sum - 10*int(self.value.count('1'))
                print("마마마마",self.name)
                print(self.hand)
                print(self.value)
                print(self.sum)           
                return self.d_pickforace(self.name)
            
            else:
                return self.calc(self.sum)

        
class Result(Game):
    def __init__(self):
        self.name
        self.finalresult=[]

            
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
        self.cardpick2(self.name)


   
card=Card()
dealer=Dealer()
try1=Game()
# result=Result()
try1.playerpick()
# print(Class[0].hand)
# print(Class[0].value)
# print(Class[1].hand)
# print(Class[1].value)
print(dealer.hand)
print(dealer.value)
try1.additionalpick()
print(dealer.hand)
print(dealer.value)

# print(dealer.hand)
# print(dealer.value)
# print(try1.cardtotal)
# print(Class[2].hand)
# print(Class[2].value)
# print(Class[3].hand)
# print(Class[3].value)
# print(dealer.value)
# print(dealer.hand)
# print(dealer.value)
