"""
Game
"""

from wrapper import Colors, Game

WIDTH = 800
HEIGHT = 600

def init(game: Game):
    # pylint: disable=unused-argument
    """
    Initialize the game
    """

def update(game: Game):
    # pylint: disable=unused-argument
    """
    Game loop
    """

def draw(game: Game):
    """
    Render the game
    """
    game.draw_rect(0, 0, 100, 100, Colors.RED)
