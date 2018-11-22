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

dealerdeck=[]
class Dealer(Card):
    def __init__(self):
        self.pick1=cardtotal.pop()
        
        if self.pick1[1] in ['J','Q','K','F']:
            self.value1 = 10
        elif 'A' in self.pick1[1]:
            self.value1 = 11
        else:
            self.value1 = int(self.pick1[1])      

    def cardpick(self):
        self.pick2=cardtotal.pop()
        if self.pick2[1] in ('J','Q','K','F'):
            self.value2 = 10
        elif 'A' in self.pick2[1]:
            self.value2 = 11
        else:
            self.value2 = int(self.pick2[1])      

        self.ready=dealerdeck.append(self.pick1 +','+ self.pick2)
        
    def scoring(self):       
            self.value = self.value1 + self.value2

playerdeck=[]
class Player(Card):
    def __init__(self):
        self.pick1=cardtotal.pop()
        
        if self.pick1[1] in ['J','Q','K','F']:
            self.value1 = 10
        elif 'A' in self.pick1[1]:
            self.value1 = 11
        else:
            self.value1 = int(self.pick1[1])      

    def cardpick(self):
        self.pick2=cardtotal.pop()
        if self.pick2[1] in ('J','Q','K','F'):
            self.value2 = 10
        elif 'A' in self.pick2[1]:
            self.value2 = 11
        else:
            self.value2 = int(self.pick2[1])      

        self.ready=playerdeck.append(self.pick1 +','+ self.pick2)
        
    def scoring(self):       
            self.value = self.value1 + self.value2

class Rule(Dealer):
    def __init__(self):
        A=dealer.value 
        if A < 16:
            playertry1=Player()
        

    def dealerrule(self):
        while A < 17:
        self.pick3=cardtotal.pop()
        if self.pick3[1] in ('J','Q','K','F'):
            self.value2 = 10
        elif 'A' in self.pick2[1]:
            self.value2 = 11
        else:
            self.value2 = int(self.pick3[1])      
    

class Result():
    def __init__(self):
        A=dealer.value 
        B=player.value
        while A =< 21:
            ask=input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\t 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(plyaer.value))
    
    def compare(self):
        while A =< 21 and B =< 21:
            if 


try1=Card()
dealer=Dealer()
print(dealer.pick1)
print(dealer.pick1[1])
dealer.cardpick()
print(dealer.pick2)
print(dealerdeck)
dealer.scoring()
print(dealer.value)



# class Player(Card):
#     def __init__(self):
#         self.start = cardtotal.pop()
#         if 'J' or 'Q' or 'K' or 'F' in self.start:
#             self.start = 10
#         elif 'A' in self.start:
#             self.start = 11
#         else:
#             self.start = int(self.start[1])       
      
#     def cardpick(self):
#         self.choice = cardtotal.pop()
#         if 'J' or 'Q' or 'K' or 'F' in self.choice:
#             self.choice = 10
#         elif 'A' in self.choice:
#             self.choice = 11
#         else:
#             self.choice = int(self.choice[1])       
      
#     def value(self):
#         self.value = self.start + self.choice
        
#     #     print(value)
#     # def value(self):

# # class CardCalc(Card):
# #     def __init_(self):
        
    
# Card()
# Player()
# Dealer()
# try1=Card()
# player1=Player()
# dealer=Dealer()
# dealer.cardpick()
# dealer.value()
# print(dealer.value)
# # try1.value()
# # print(choice)

# # try1.value()




# # choice1=cardtotal.pop(0)

# # if 'A' in choice1: 
# #     choice1 = choice1[0] + '11' 
# # if 'J' in choice1: 
# #     choice1 = choice1[0] + '10' 
# # if 'Q' in choice1: 
# #     choice1 = choice1[0] + '10' 
# # if 'K' in choice1: 
# #     choice1 = choice1[0] + '10' 
# # if 'F' in choice1: 
# #     choice1 = choice1[0] + '10' 


# # choice2=cardtotal.pop(0)

# # if 'A' in choice2: 
# #     choice2 = choice2[0] + '11' 
# # if 'J' in choice2: 
# #     choice2 = choice2[0] + '10' 
# # if 'Q' in choice2: 
# #     choice2 = choice2[0] + '10' 
# # if 'K' in choice2: 
# #     choice2 = choice2[0] + '10' 
# # if 'F' in choice2: 
# #     choice2 = choice2[0] + '10' 

# # if len(choice1)<=2:
# #     a = int(choice1[1])
# # else:
# #     a=10

# # if len(choice2)<=2:
# #     b = int(choice2[1])
# # else:
# #     b=10

# # cardvalue = a + b
# # print(cardvalue)



# # tyrthis=ValueSum()
