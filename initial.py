from wrapper import Game, Colors
import pygame

WIDTH = 1200
HEIGHT = 800

is_first_time = True

def handle_event(g: Game, event):
    pass

def init(g: Game):
    global is_first_time
    if not is_first_time:
        return
    is_first_time = False

def update(g: Game, dt: float):
    init(g)

def draw(g: Game):
    g.draw_background(Colors.BLACK)
