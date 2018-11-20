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
        self.picklikst=self.deck.append(self.pick)
    
    def cardpick2(self):
        self.pick2=cardtotal.pop()
        self.picklist=self.deck.append(self.pick2)
        
    
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


class Dealer(Card):
    def __init__(self):
        self.deck=[]
    

class Player(Card):
    def __init__(self):
        self.deck=[]
        
    def asking(self):
        # while True:
            if 11 not in self.deck:
                ask=input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.sum))
                if ask == 'H':
                    self.cardpick()
                    self.scoring()
                    print(self.deck)
                    print(self.sum)
                    # continue
                
                elif ask == 'S': 
                    self.result=self.sum
                    print(self.deck)
                    print(self.result)

                    # break

                
            if 11 in self.deck:
                ask=input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.sum))
                if ask == 'H':
                    self.cardpick()
                    self.scoring()
                    print(self.deck)
                    print(self.sum)
                    # continue

                elif ask == 'S':
                    if self.deck.count(11)>2:
                        question=input("에이스가 {} 개 있네요. 무엇으로 하시겠습니까? '1' 또는 '11'을 차례대로 입력해주세요!\n 'AA'일 경우 '11,11' 혹은 '1,1 (콤마로구분)".format(self.deck.count(11)))
                        acechoice=question.split(',')
                        for i in range(len[acechoice]):
                            choiceassign=[]
                            choiceassign=choiceassign.append(acechoice[i-1])
                            if '11' in choiceassign:
                                result=self.sum - 10*int(choiceassign.count('11'))
                            else:
                                result=self.sum
                    else:
                        result=self.sum
                    # break




        
        # else: 
        #     input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\t 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.sum))
        # elif self.sum <= 21 and 11 in self.deck:
        #     input("에이스는 뭘로 할래요?")
        # else:
        #     print("아직하는중")

try1=Card()
# dealer=Dealer()
player=Player()
# dealer.cardpick()
# dealer.cardpick2()
player.cardpick()
player.cardpick2()
print('11111',player.deck)
player.scoring()
player.asking()
print('22222',player.deck)
print('33333',player.sum)
print('4444',player.pick)
