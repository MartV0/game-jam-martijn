from flight.coordinates import *
from jorcademy import *
import flight.bullet as bullet


def update_fireballs(plane):
    bullet.update_bullets(plane)
    for fireball in plane.bullets:
        try:
            fireball.gravity += 0.5
        except AttributeError:
            fireball.gravity = 0
        fireball.y += fireball.gravity


def draw_fireballs(fireballs):
    for fireball in fireballs:
        image("flight/fireball.png", fireball.x, fireball.y, 3, 0)


def fireball_collisions(plane, ghosts):
    bullet.bullet_collisions(plane, ghosts)
