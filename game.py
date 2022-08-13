from wrapper import Game, Colors
import pygame
from random import randint, choice
from math import sqrt

WIDTH = 1200
HEIGHT = 800

is_first_time = True

def handle_event(g: Game, ev):
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
        g.ml = True
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
        g.mr = True

    if ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
        g.ml = False
    if ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
        g.mr = False

    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
        global is_first_time
        is_first_time = True
        init(g)

def init(g: Game):
    g.score = 0
    g.game_over = False

    g.r = 50
    g.x = randint(g.r / 2, WIDTH - g.r / 2)
    g.y = 100

    g.vx = choice([-1, 1]) * (4 + randint(0, 7))
    g.vy = choice([-1, 1]) * (4 + randint(0, 7))

    g.wp = 150
    g.hp = 50
    g.px = WIDTH / 2

    g.vp = 15
    g.ml = False
    g.mr = False

def update(g: Game, dt: float):
    if g.game_over:
        return

    # Collision
    if g.y + g.r >= HEIGHT - g.hp:
        r2 = g.hp
        left_collides = g.px - g.wp / 2 <= (g.x - g.r) <= g.px + g.wp / 2
        right_collides = g.px - g.wp / 2 <= (g.x + g.r) <= g.px + g.wp / 2
        d1 = sqrt((g.x - g.px - g.wp / 2 + r2) ** 2 + (g.y - HEIGHT - g.hp / 2) ** 2)
        d2 = sqrt((g.x - g.px + g.wp / 2 - r2) ** 2 + (g.y - HEIGHT - g.hp / 2) ** 2)
        collides_circle = (d1 <= r2 + g.r) or (d2 <= r2 + g.r)
        
        if left_collides or right_collides or collides_circle:
            g.vy = -g.vy

            inc = 1.1

            g.vx *= inc
            g.vy *= inc
            g.score += 1
        else:
            g.game_over = True

    if not (g.ml and g.mr):
        if g.ml:
            g.px -= g.vp
        if g.mr:
            g.px += g.vp

    if g.x - g.r <= 0 or g.x + g.r >= WIDTH:
        g.vx = -g.vx
    
    if g.y - g.r <= 0:
        g.vy = -g.vy

    if g.y + g.r >= HEIGHT:
        g.game_over = True

    min_x = g.wp / 2
    max_x = WIDTH - g.wp / 2
    
    g.px = min(max(min_x, g.px), max_x)

    g.vy += 20

    g.vx += 10.0

    g.x += g.vx * dt
    g.y += g.vy * dt


def draw(g: Game):
    font_size = 120
    g.draw_background(Colors.BLACK)
    g.draw_text(str(g.score), WIDTH / 2, font_size / 2, font_size, Colors.WHITE)
    if not g.game_over:
        g.draw_circle(g.x, g.y, g.r, Colors.RED)
        g.draw_rect(g.px, HEIGHT - g.hp / 2, g.wp, g.hp, Colors.BLUE)
