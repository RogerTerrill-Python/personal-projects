
class Card:
    def __init__(self, value, face, suit):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f'Suit value of: {self.suit} Face value of {self.face} Value of {self.value}'
