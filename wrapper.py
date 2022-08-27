"""
Wrapper over pygame
"""

import pygame
from collections.abc import Callable

class Colors:
    """
    Color class
    """
    # pylint: disable=too-few-public-methods
    RED: tuple[int, int, int] = (255, 0, 0)
    GREEN : tuple[int, int, int] = (0, 255, 0)
    BLUE : tuple[int, int, int] = (0, 0, 255)
    WHITE : tuple[int, int, int] = (255, 255, 255)
    BLACK : tuple[int, int, int] = (0, 0, 0)
    MAGENTA : tuple[int, int, int] = (255, 0, 255)
    YELLOW : tuple[int, int, int] = (255, 255, 0)
    CYAN : tuple[int, int, int] = (0, 255, 255)
    ORANGE : tuple[int, int, int] = (255, 165, 0)
    BROWN : tuple[int, int, int] = (165, 42, 42)
    GRAY : tuple[int, int, int] = (128, 128, 128)
    DARK_GRAY : tuple[int, int, int] = (64, 64, 64)
    LIGHT_GRAY : tuple[int, int, int] = (192, 192, 192)
    DARK_BLUE : tuple[int, int, int] = (0, 0, 128)
    DARK_GREEN : tuple[int, int, int] = (0, 128, 0)
    DARK_CYAN : tuple[int, int, int] = (0, 128, 128)
    DARK_RED : tuple[int, int, int] = (128, 0, 0)
    DARK_MAGENTA : tuple[int, int, int] = (128, 0, 128)
    DARK_YELLOW : tuple[int, int, int] = (128, 128, 0)
    DARK_ORANGE : tuple[int, int, int] = (128, 128, 0)
    DARK_BROWN : tuple[int, int, int] = (128, 64, 64)
    GREEN_YELLOW : tuple[int, int, int] = (128, 255, 0)
    BLUE_YELLOW : tuple[int, int, int] = (0, 255, 128)
    BLUE_GREEN : tuple[int, int, int] = (0, 128, 128)
    RED_YELLOW : tuple[int, int, int] = (255, 128, 0)
    RED_GREEN : tuple[int, int, int] = (128, 128, 0)
    PINK : tuple[int, int, int] = (255, 192, 203)
    PINK_YELLOW : tuple[int, int, int] = (255, 228, 225)
    PINK_GREEN : tuple[int, int, int] = (0, 255, 255)
    PINK_BLUE : tuple[int, int, int] = (0, 0, 255)
    PINK_RED : tuple[int, int, int] = (255, 0, 255)
    PINK_MAGENTA : tuple[int, int, int] = (255, 0, 255)
    PINK_CYAN : tuple[int, int, int] = (0, 255, 255)

ALL_COLORS: list[tuple[int, int, int]] = [
    Colors.RED,
    Colors.GREEN,
    Colors.BLUE,
    Colors.WHITE,
    Colors.BLACK,
    Colors.MAGENTA,
    Colors.YELLOW,
    Colors.CYAN,
    Colors.ORANGE,
    Colors.BROWN,
    Colors.GRAY,
    Colors.DARK_GRAY,
    Colors.LIGHT_GRAY,
    Colors.DARK_BLUE,
    Colors.DARK_GREEN,
    Colors.DARK_CYAN,
    Colors.DARK_RED,
    Colors.DARK_MAGENTA,
    Colors.DARK_YELLOW,
    Colors.DARK_ORANGE,
    Colors.DARK_BROWN,
    Colors.GREEN_YELLOW,
    Colors.BLUE_YELLOW,
    Colors.BLUE_GREEN,
    Colors.RED_YELLOW,
    Colors.RED_GREEN,
    Colors.PINK,
    Colors.PINK_YELLOW,
    Colors.PINK_GREEN,
    Colors.PINK_BLUE,
    Colors.PINK_RED,
    Colors.PINK_MAGENTA,
    Colors.PINK_CYAN
]

VIVID_COLORS: list[tuple[int, int, int]] = [
    Colors.RED,
    Colors.GREEN,
    Colors.BLUE,
    Colors.WHITE,
    Colors.MAGENTA,
    Colors.YELLOW,
    Colors.CYAN,
    Colors.ORANGE,
    Colors.GREEN_YELLOW,
    Colors.RED_YELLOW,
    Colors.RED_GREEN,
    Colors.PINK,
]

# Set up the drawing window
pygame.init()
pygame.font.init()

class GameObject:
    def __init__(self, screen):
        self.screen = screen

    def draw_text(self, text: str, x: float, y: float, size: int, color: tuple[int, int, int]):
        font = pygame.font.SysFont("Arial", size)
        text_surface = font.render(text, False, color)
        szx, szy = font.size(text)
        self.screen.blit(text_surface, (x - szx / 2, y - szy / 2))

    def draw_rect(self, x: float, y: float, width: int, height: int, color: tuple[int, int, int]):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a rectangle
        """
        pygame.draw.rect(self.screen, color, (int(x) - width // 2, int(y) - height // 2, width, height))

    def draw_circle(self, x: float, y: float, radius: int, color: tuple[int, int, int]):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a circle
        """
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, color: tuple[int, int, int], width: int):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a line from (x1, y1) -> (x2, y2)
        """
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), width)

    def draw_background(self, color: tuple[int, int,  int]):
        self.screen.fill(color)


class Game:
    """
    Abstraction over a pygame game
    """

    def __init__(self, init: Callable[[GameObject], None], handle_event: Callable[[GameObject, pygame.event.Event], None], update: Callable[[GameObject, float], None], draw: Callable[[GameObject], None], width: int, height: int):
        # pylint: disable=too-many-arguments
        self.update = update
        self.init = init
        self.handle_event = handle_event
        self.draw = draw
        self.screen = pygame.display.set_mode([width, height])
        self.game_object = GameObject(self.screen)

    def run(self):
        """
        Starts the game loop
        """

        self.init(self.game_object)

        clock = pygame.time.Clock()

        # Import and initialize the pygame library
        # Run until the user asks to quit
        self.last = pygame.time.get_ticks()
        running = True
        while running:
            last = self.last
            self.last = pygame.time.get_ticks()
            # Did the user click the window close button?
            for event in pygame.event.get():
                self.handle_event(self.game_object, event)
                if event.type == pygame.QUIT:
                    running = False

            self.update(self.game_object, (self.last - last) / 1000.0)
            self.draw(self.game_object)

            # Flip the display
            pygame.display.flip()

            # Wait a bit (60 FPS)
            clock.tick(60)

        # Done! Time to quit.
        pygame.quit()
