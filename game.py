import time
import random
# from IPython.display import clear_output
class Game:
    def __init__(self, dealer, player):
        self.deck = self.set_deck()
        self.dealer = dealer
        self.player = player

    def set_deck():
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        names = [2,3,4,5,6,7,8,9,10, 'jack', 'King', 'Queen', 'Ace']
        deck = [(suits, names) for suit in suits for name in names]
        random.shuffle(deck)
        return deck

    def cards_passed():
        if self.set_deck() > 7:
            


class Card:
    def __init__(self, cards):
        self.cards = cards
        self.random_cards = []
        for card in cards:
            self.random_cards.append(card)

    def __str__(self):
        return "f{self.card} is your card" 

    def dealing(self):
        single_card = self.card.pop()
        return single_card

class Human:
    def __int__(self, dealer, player):
        self.dealer = dealer
        self.player = player
        self.cards = []
        
    def adding_card(self, card):
        self.cards.append(card)

# call the function right here to play the game 
def play_game():
    while True:
        i = input("Do you want to Play? Enter 'yes' or 'no' please. ")
        if i == 'yes':
            print(f"These are your cards.{Game.set_deck()}")
            x = input("Do you want to 'hit' or 'bust'? ")
            if x == 'bust':
                print('Thanks for playing')
                break
        if i == 'no':
            print(f"Have a good day, Your total was")
            break
        

play_game()