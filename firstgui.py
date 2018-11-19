class Card:
    def __init__(self):
        self.name='kkkk'
        print("111111")

class Deck(Card):
    def printsome(self):
        print('1','2','3')


card=Card()
deck=Deck()
deck.printsome()