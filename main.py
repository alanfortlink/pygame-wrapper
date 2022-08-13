"""
Main file for the game
"""

from wrapper import Game
from game import handle_event, update, draw, WIDTH, HEIGHT

def main():
    """
    Main function
    """
    game: Game = Game(handle_event, update, draw, WIDTH, HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
