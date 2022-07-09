"""
Main file for the game
"""

from wrapper import Game
from game import init, update, draw, WIDTH, HEIGHT

def main():
    """
    Main function
    """
    game: Game = Game(init, update, draw, WIDTH, HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
