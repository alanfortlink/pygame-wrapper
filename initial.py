from wrapper import Game, Colors

WIDTH = 1200
HEIGHT = 800

# Called upon an event (Mouse, Keyboard, Joystick)
def handle_event(g: Game, event):
    pass

# Called once before the start of the game
def init(g: Game):
    pass

# Called every frame to update the state
def update(g: Game, dt: float):
    pass

# Called every frame to draw the frame
def draw(g: Game):
    g.draw_background(Colors.BLACK)
