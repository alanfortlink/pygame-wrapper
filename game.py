from typing_extensions import Self
from wrapper import GameObject, Colors
import pygame
from random import randint

WIDTH = 1200
HEIGHT = 800

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def mul(self, scalar: float) -> Self: return Vector(self.x * scalar, self.y * scalar)

class Element:
    def __init__(self, position: Vector, width: int, height: int, speed: Vector, color: tuple[int, int, int]):
        self.position = position
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color

    def update(self, g: GameObject, dt: float):
        self.position = self.position + self.speed.mul(dt)

    def lock(self, p1x: float, p1y: float, p2x: float, p2y: float) -> None:
        self.position.x = min(p2x, max(p1x, self.position.x))
        self.position.y = min(p2y, max(p1y, self.position.y))

    def bounce(self, p1x: float, p1y: float, p2x: float, p2y: float) -> None:
        if self.position.x <= p1x or self.position.x >= p2x:
            self.speed.x = -self.speed.x
        if self.position.y <= p1y or self.position.y >= p2y:
            self.speed.y = -self.speed.y

player_speed = 1000
key_pressed = {}

player = Element(Vector(100, 100), 50, 50, Vector(0, 0), Colors.RED)
enemy = Element(Vector(WIDTH - 100, HEIGHT - 100), 50, 50, Vector(randint(80, 120), randint(80, 120)), Colors.BLUE)

def handle_event(g: GameObject, event: pygame.event.Event):
    if event.type == pygame.KEYDOWN:
        key_pressed[event.key] = True
    if event.type == pygame.KEYUP:
        key_pressed[event.key] = False

def init(_: GameObject):
    for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
        key_pressed[key] = False

def update(g: GameObject, dt: float):
    player.speed = Vector(key_pressed[pygame.K_LEFT] * -player_speed + key_pressed[pygame.K_RIGHT] * player_speed,
                        key_pressed[pygame.K_UP] * -player_speed + key_pressed[pygame.K_DOWN] * player_speed)

    player.update(g, dt)
    player.lock(player.width / 2, player.height / 2, WIDTH - player.width / 2, HEIGHT - player.height / 2)

    enemy.update(g, dt)
    enemy.bounce(enemy.width / 2, enemy.height / 2, WIDTH - enemy.width / 2, HEIGHT - enemy.height / 2)

def draw(g: GameObject):
    g.draw_background(Colors.BLACK)
    g.draw_rect(player.position.x, player.position.y, player.width, player.height, player.color)
    g.draw_rect(enemy.position.x, enemy.position.y, enemy.width, enemy.height, enemy.color)
