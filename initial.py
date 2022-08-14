from wrapper import GameObject, Colors
import pygame

WIDTH = 1200
HEIGHT = 800

# Called upon an event (Mouse, Keyboard, Joystick)
def handle_event(g: GameObject, event: pygame.event.Event):
    pass

# Called once before the start of the game
def init(g: GameObject):
    pass

# Called every frame to update the state
def update(g: GameObject, dt: float):
    pass

# Called every frame to draw the frame
def draw(g: GameObject):
    g.draw_background(Colors.BLACK)
    g.draw_circle(100, 100, 50, Colors.RED)
