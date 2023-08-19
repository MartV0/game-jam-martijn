from jorcademy import *
from flight.coordinates import *
import random


ghosts = []


class Ghost:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed


def update_ghosts():
    roll = random.randint(0,120)
    if roll == 20:
        x = random.randint(0, w)
        y = random.randint(0, h)
        d = random.randint(0, 359)
        ghosts.append(Ghost(x, y, d, 0))
    for ghost in ghosts:
        ghost.direction += random.randint(-10,10)
        vx, vy = get_direction_vector(ghost.direction, False)
        speed = 2
        ghost.x += speed * vx
        ghost.y += speed * vy
        if is_offscreen(ghost.x, ghost.y):
            ghost.direction = bounce_angle(ghost.direction)
        ghost.x, ghost.y = teleport_if_offscreen((ghost.x, ghost.y), False)


def draw_ghosts():
    for ghost in ghosts:
        # ellipse((0,255,0), ghost.x, ghost.y, 57, 57) 
        image("flight/ghost.png", ghost.x, ghost.y, 4, 0)
