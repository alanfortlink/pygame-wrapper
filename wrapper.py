"""
Wrapper over pygame
"""

import pygame

class Colors:
    """
    Color class
    """
    # pylint: disable=too-few-public-methods
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    MAGENTA = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    ORANGE = (255, 165, 0)
    BROWN = (165, 42, 42)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    LIGHT_GRAY = (192, 192, 192)
    DARK_BLUE = (0, 0, 128)
    DARK_GREEN = (0, 128, 0)
    DARK_CYAN = (0, 128, 128)
    DARK_RED = (128, 0, 0)
    DARK_MAGENTA = (128, 0, 128)
    DARK_YELLOW = (128, 128, 0)
    DARK_ORANGE = (128, 128, 0)
    DARK_BROWN = (128, 64, 64)
    GREEN_YELLOW = (128, 255, 0)
    BLUE_YELLOW = (0, 255, 128)
    BLUE_GREEN = (0, 128, 128)
    RED_YELLOW = (255, 128, 0)
    RED_GREEN = (128, 128, 0)
    PINK = (255, 192, 203)
    PINK_YELLOW = (255, 228, 225)
    PINK_GREEN = (0, 255, 255)
    PINK_BLUE = (0, 0, 255)
    PINK_RED = (255, 0, 255)
    PINK_MAGENTA = (255, 0, 255)
    PINK_CYAN = (0, 255, 255)

ALL_COLORS = [
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

# Set up the drawing window
pygame.init()
pygame.font.init()
class Game:
    """
    Abstraction over a pygame game
    """

    def __init__(self, init, handle_event, update, draw, width, height):
        # pylint: disable=too-many-arguments
        self.update = update
        self.init = init
        self.handle_event = handle_event
        self.draw = draw
        self.screen = pygame.display.set_mode([width, height])

    def draw_text(self, text, x, y, size, color):
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, False, color)
        szx, szy = font.size(text)
        self.screen.blit(text_surface, (x - szx / 2, y - szy / 2))

    def draw_rect(self, x, y, width, height, color):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a rectangle
        """
        pygame.draw.rect(self.screen, color, (x - width / 2, y - height / 2, width, height))

    def draw_circle(self, x, y, radius, color):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a circle
        """
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def draw_background(self, color):
        self.screen.fill(color)

    def run(self):
        """
        Starts the game loop
        """

        self.init(self)
        # Set 60 frames per second
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
                self.handle_event(self, event)
                if event.type == pygame.QUIT:
                    running = False

            self.update(self, (self.last - last) / 1000.0)
            self.draw(self)

            # Flip the display
            pygame.display.flip()

            # Wait a bit
            clock.tick(60)

        # Done! Time to quit.
        pygame.quit()
