from wrapper import GameObject, Colors
import pygame

WIDTH = 1200
HEIGHT = 800


def handle_event(g: GameObject, event: pygame.event.Event):
    """Called for every event (Mouse, Keyboard, Joystick)"""
    pass


def init(g: GameObject):
    """Called once before the start of the game"""


def update(g: GameObject, dt: float):
    """Called every frame to update the state"""


def draw(g: GameObject):
    """Called every frame to draw the frame"""

    g.draw_background(Colors.BLACK)
    g.draw_circle(100, 100, 50, Colors.RED)
