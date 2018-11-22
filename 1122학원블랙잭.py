import random


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
        # self.cardtotal
        for i in playerinit:
            i=Player(i)
            # playerclass.append(i)
        self.name=i

    def valueassign(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10'
        
        elif 'A' in card[1]:
            self.eachvalue = '11'
        
        else:
            self.eachvalue = card[1]

        return self.eachvalue   
    
    def cardpick(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.valueassign(self.carddraw)
        self.value.append(self.eachvalue)

    
    def cardpick2(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.valueassign(self.carddraw)
        self.value.append(self.eachvalue)
        print("{}님 카드{} 뽑으셨네요 ? 현재카드는{}입니다.".format(self.name,self.carddraw,self.hand))

    def dealerpick(self):
        self.cardpick(self.name)
        self.dealerscoring(self.hand, self.value)
     
    def playerpick(self):
        for i in playerclass:
            i.cardpick(i.name)
 
    def additionalpick(self):
        for i in playerclass:
            i.cardpick(i.name)
        self.cardpick(self.name)
    
    
    
    
    
    def waitingfordealer(self, name, hand, value):
        self.p_sum=0
        self.name=name
        self.hand=hand
        self.value=value
        for i in self.value:
            self.p_sum+=int(i)
    
        self.scoringstep(self.name, self.hand, self.value)

                
    
    def scoringstep(self, name, hand, value):
        return Scoring(name,hand,value) 

    # def calc(self, name, hand, value, finalresult):
    #     self.name=name
    #     self.hand=hand
    #     self.value=value
    #     self.finalresult=finalresult

    def finalscore(self, name, hand, value, finalresult):        
        if finalresult > 21:
            print("{}님 카드{}은 21이 넘었네???ㅋㅋㅋㅋㅋ일단졌습니다. 디~지세요".format(self.name,self.hand))
        
        elif finalresult == 21:
            print("{}님 카드{}은 블랙잭이네요.  딜러의 결과를 기다려 봅시다. 겁나게운좋네".format(self.name,self.hand))
    
        else:
            name=[]
            hand=[]
            finalresult=[]
            for i in finalresult:
                i=max(finalresult)
                print(i)
                # indexvalue=(finalresult.index(i))
            # print(name[indexvalue])
            # print(hand[indexvalue])
            # print("{}님이 {}조합으로 이기셨습니다.".format(name[indexvalue],hand[indexvalue]))
        
class Scoring(Game):
    def __init__(self, name, hand, value):
        self.p_sum=0
        self.name=name
        self.hand=hand
        self.value=value
        for i in self.value:
            self.p_sum+=int(i)
        self.playerlogic(self.name, self.hand, self.value, self.p_sum)

       
    def playerlogic(self, name, hand, value, p_sum):
        # self.finalresult=0
        if '11' in value:
            value.count('11')
            question=input("{}님 에이스가 {} 개 있네요. {} 무엇으로 하시겠습니까? 1개면 원하는 숫자를\n 두개이상이면 '1' 또는 '11'을 차례대로 입력해주세요!\n 'AA'일 경우 '11,11' 혹은 '1,1 (콤마로구분)".format(self.name, value.count('11'),hand))
            if question == '1':
                    p_sum=p_sum - 10*int(choiceassign.count('11'))
                    return self.finalscore(self.name, self.hand, self.value, self.p_sum)

            elif question =='11':
                return self.finalscore(self.name, self.hand, self.value, self.p_sum)    
            
            else:
                acechoice=question.split(',')
                for i in acechoice:
                    choiceassign=[]
                    choiceassign=choiceassign.append(i)
                    if '11' in choiceassign:
                        p_sum=p_sum - 10*int(choiceassign.count('11'))
                        return self.finalscore(self.name, self.hand, self.value, self.p_sum)
                    
                    else:
                        p_sum
                        return self.finalscore(self.name, self.hand, self.value, self.p_sum)
       
        else:
            return self.finalscore(self.name, self.hand, self.value, self.p_sum)


     
class Result(Scoring):
    def __init__(self, name, hand, value):
        self.name=name
        self.hand=hand
        self.value=value

class Player(Game):
    def __init__(self,i):
        self.name=i
        self.hand=[]
        self.value=[]
        print("{}가 플레이합니다".format(i))

    def choiceforgame(self, name, hand, value):
            msg=input("{}님 카드를 더 받으시겠습니까? 현재카드는{}입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(name, hand))
            if msg == 'S':
                playerclass.remove(i)
                activeplayernumber=playernumber-1
                return self.waitingfordealer(self.name, self.hand, self.value)
            
            elif msg == 'H': 
                return self.cardpick2(self.name)
            
            else:
                return msg        

    def waitingforscoring(self, name, hand, value):
        self.scoringstep(self.name, self.hand, self.value)


class Dealer(Game):
    hand=[]
    value=[]
    def __init__(self):
        self.name='나는딜러다'
        
    def give1stcard(self):
       self.playerpick()
       self.cardpick(self.name)

    def give2ndcard(self):
        self.additionalpick()

    def dealerscoring(self, hand, value):
        self.valuesum=0
        self.hand=hand
        self.value=value
        for i in self.value:
            self.valuesum+=int(i)
        return self.dealerlogic(self.value, self.valuesum)
    

    def d_valueforace(self, card):
        if card[1] in ['J','Q','K','F'] : 
            self.eachvalue = '10'
        elif 'A' in card[1]:
            self.eachvalue = '11'
        else:
            self.eachvalue = card[1]
        return self.eachvalue  
    
    def d_pickforace(self, name):
        self.carddraw=self.cardtotal.pop(0)
        self.hand.append(self.carddraw)
        self.d_valueforace(self.carddraw)
        self.value.append(self.eachvalue)

    def dealerlogic(self, value, valuesum):
        while '11' not in value:
            if valuesum >= 17:
                print("가가가",self.name)
                return  self.finalscore(self.name, self.hand, self.value, self.valuesum)
            
            elif valuesum < 17:
                print("나나나",self.name)
                return self.cardpick(self.name)
                  
        while '11' in self.value:   
            if valuesum == 21:
                print("다다다",self.name)
                return self.finalscore(self.name, self.hand, self.value, self.valuesum)                  
            
            elif valuesum < 17:
                print("라라라",self.name)
                return self.cardpick(self.name)
            
            elif valuesum > 21:
                self.value.remove('11')
                self.value.append('1')

                self.valuesum=self.valuesum - 10*int(self.value.count('1'))
                print("마마마마",self.name)
                print(self.hand)
                print(self.value)
                print(self.valuesum)           
                return self.d_pickforace(self.name)
            
            else:
                return self.finalscore(self.name,self.hand, self.value, self.valuesum)



    
#---------------------이하 mainflow-----------------------   
playernumber=7
playerinit=['김일수','김이수', '김삼수','김사수','김오수','김육수','김칠수']
playerclass=[]
a=7


card=Card()
dealer=Dealer()
game=Game()
dealer.give1stcard()
dealer.give2ndcard()


activeplayer=[]
while True:

    for i in playerclass:
        i.choiceforgame(i.name,i.hand, i.value)

    dealer.cardpick(dealer.name)                
    



        
        else:
            for i in activeplayer:
                i.choiceforgame(i.name,i.hand,i.value)
                dealer.cardpick(dealer.name)
                continue

        


# while playernumber > 0:

# for i in playerclass:
#     i.scoringstep(i.name,i.hand,i.value)
# for i in playerclass:        
#     i.playerlogic(i.name, i.hand, i.value, i.sum)

