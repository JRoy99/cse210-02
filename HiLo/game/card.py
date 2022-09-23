import random


class Card:
    """A card with a value between 1 and 13.

    The responsibility of Card is to keep track of the card value.

    Attributes:
        value (int): The value of the card drawn.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        
    def draw(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randrange(1, 13, 1)