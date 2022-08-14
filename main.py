"""
Main file for the game
"""

from wrapper import Game
from initial import init, handle_event, update, draw, WIDTH, HEIGHT

def main():
    """
    Main function
    """
    game: Game = Game(init, handle_event, update, draw, WIDTH, HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
