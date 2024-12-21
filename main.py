from phevaluator.evaluator import evaluate_cards
import random

SUITS = ["s", "h", "d", "c"]
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class Player:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

def get_cards(deck, n):
    cards = []
    for _ in range(n):
        card = random.choice(deck)
        deck.remove(card)
        cards.append(card)
    return deck, cards

def test(c1, c2, num_others):
    deck = [(c + s) for c in CARDS for s in SUITS]
    deck.remove(c1)
    deck.remove(c2)

    others = []
    others_scores = []

    for _ in range(num_others):
        deck, cards = get_cards(deck, 2)
        others.append(Player(cards[0], cards[1]))

    deck, comm_cards = get_cards(deck, 5)

    for other in others:
        other_score = evaluate_cards(other.c1, other.c2, comm_cards[0], comm_cards[1], comm_cards[2], comm_cards[3], comm_cards[4])
        others_scores.append(other_score)

    c_score = evaluate_cards(c1, c2, comm_cards[0], comm_cards[1], comm_cards[2], comm_cards[3], comm_cards[4])

    for other_score in others_scores:
        if other_score < c_score:
            return False
    return True

if __name__ == "__main__":
    c1 = input("Card 1: ")
    c2 = input("Card 2: ")
    c3 = input("How many other players will there be? ")

    sim_size = input("How many simulations would you like to run? ")

    win = 0
    lose = 0

    for _ in range(int(sim_size)):
        result = test(c1, c2, int(c3))
        if result:
            win += 1
        else:
            lose += 1

    print(f"Your cards: {c1}, {c2}")
    print(f"Other opponents: {c2}")
    print(f"Simulation size: {sim_size}")
    print(f"Win chance: {round((win / (win + lose)) * 100, 2)}%")