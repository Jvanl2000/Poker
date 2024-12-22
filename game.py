import random

class Game:
    def __init__(self, amt_others, deck, **kwargs):
        self.deck = deck
        
        self.s1 = kwargs.get("s1", None)
        self.s2 = kwargs.get("s2", None)

        self.comm_cards = kwargs.get("comm_cards", None)

        self.others = []
        for i in range(1, amt_others + 1):
            card1 = kwargs.get(f"p{i}1", None)
            card2 = kwargs.get(f"p{i}2", None)
            self.others.append([card1, card2])

        try:
            self.deck.remove(self.s1)
            self.deck.remove(self.s2)
            for card in self.comm_cards:
                self.deck.remove(self)



    def generate_value(self):
        if self.s1 == None:
            card = random.choice(self.deck)
            self.deck.remove(card)
            self.s1 = card
        elif self.s2 == None:
            card = random.choice(self.deck)
            self.deck.remove(card)
            self.s2 = card
        


SUITS = ["s", "h", "d", "c"]
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

deck = [(c + s) for c in CARDS for s in SUITS]

game = Game(2, deck, s1="Ks", s2="Kd",p11="As", p12="Ac", p21="Ah", p22="Ad")