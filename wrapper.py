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

# Set up the drawing window
pygame.init()
class Game:
    """
    Abstraction over a pygame game
    """

    def __init__(self, init, update, draw, width, height):
        # pylint: disable=too-many-arguments
        self.init = init
        self.update = update
        self.draw = draw
        self.screen = pygame.display.set_mode([width, height])

    def draw_rect(self, x, y, width, height, color):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a rectangle
        """
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw_circle(self, x, y, radius, color):
        # pylint: disable=too-many-arguments,invalid-name
        """
        Draws a circle
        """
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def run(self):
        """
        Starts the game loop
        """

        self.init(self)

        # Set 60 frames per second
        clock = pygame.time.Clock()

        # Import and initialize the pygame library
        # Run until the user asks to quit
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update(self)

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            self.draw(self)

            # Flip the display
            pygame.display.flip()

            # Wait a bit
            clock.tick(60)

        # Done! Time to quit.
        pygame.quit()
