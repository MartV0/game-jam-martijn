from flight.coordinates import *
from jorcademy import *


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def update_bullets(plane):
    plane.bulletdelay -= 1
    if is_key_down('b') and plane.bulletdelay <= 0:
        plane.bulletdelay=10
        plane.bullets.append(create_bullet(plane))
    for bullet in plane.bullets:
        move_bullet(bullet)
    plane.bullets = [bullet for bullet in plane.bullets if not is_offscreen(bullet.x, bullet.y)]


def move_bullet(bullet):
    xv, yv = get_direction_vector(bullet.direction)
    bullet_speed = 20
    bullet.x += bullet_speed * xv
    bullet.y += bullet_speed * yv


def create_bullet(plane):
    angle = plane.angle
    if plane.right:
        angle += 180
    return Bullet(plane.x, plane.y, angle)


def draw_bullets(bullets):
    for bullet in bullets:
        ellipse((255,255,0), bullet.x, bullet.y, 20, 20)


def bullet_collisions(plane, ghosts):
    bullet_radius = 10
    # for simplicitys sake we threat the ghosts as circles during intersections
    ghost_radius = 28.5 
    for bullet in plane.bullets:
        for ghost in ghosts:
            d = distance(ghost.x, ghost.y, bullet.x, bullet.y)
            if d < bullet_radius + ghost_radius:
                ghosts.remove(ghost)
                plane.bullets.remove(bullet)
