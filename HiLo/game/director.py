from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        last_card (Card): The first card drawn during play.
        next_card (Card): The current/last card drawn during play.
        is_playing (boolean): Whether or not the game is being played.
        guess (string): Player's last guess for if the subsequent card is higher or lower.
        correct (boolean): Whether or not he player's guess was correct.
        points (int): The current points for the player.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.last_card = Card()
        self.next_card = Card()
        self.is_playing = True
        self.guess = ""
        self.correct = False
        self.points = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if the next card will be higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        self.last_card.draw()
        print(f"The card is: {self.last_card.value}")
        self.guess = input("Higher or lower? [h/l] ")
        while self.guess != "h" or "l":
            self.guess = input("Invalid input. Please select higher or lower [h/l] ")
        
       
    def do_updates(self):
        """Updates the player's points, losing on a draw.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        self.next_card.draw()
        self.correct = (((self.last_card.value > self.next_card.value) and (self.guess == "l")) or 
            ((self.last_card.value < self.next_card.value) and (self.guess == "h")))

        if self.correct:
            points += 100
        else:
            points -= 75

    def do_outputs(self):
        """Displays the card and any change in points. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.next_card.value}")
        print(f"Unlucky! It's a draw.")
        print(f"Your score is: {self.points}\n")
        self.is_playing == (self.points > 0)

        self.is_playing = (input("Play again? [y/n] ") == "y")