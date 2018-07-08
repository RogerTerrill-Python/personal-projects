import random


class Card:
    def __init__(self, value, face, suit):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f'Suit: {self.suit:<10} Face: {self.face:<10} Value: {self.value}'


class Deck:
    def __init__(self):
        self.cards = []

    def make_deck(self):
        values = [1, 2, 3, 4]
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        faces = ['Ace', 'Two', 'Three', 'Four']

        for card in range(4):
            self.cards.append(Card(values[card], faces[card], suits[card]))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)


def main():
    player_deck = Deck()
    player_deck.make_deck()
    player_deck.print_deck()
    print('===AFTER SHUFFLE===')
    player_deck.shuffle_deck()
    player_deck.print_deck()


if __name__ == '__main__':
    main()
