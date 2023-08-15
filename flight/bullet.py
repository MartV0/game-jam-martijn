from flight.coordinates import *
from jorcademy import *


bullets = []
bulletdelay = 0


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def update_bullets(plane2):
    global bulletdelay
    bulletdelay -= 1
    if is_key_down('b') and bulletdelay <= 0:
        bullets.append(Bullet(plane2.x, plane2.y, plane2.angle))
        bulletdelay=10
    for bullet in bullets:
        xv, yv = get_direction_vector(bullet.direction, plane2.right)
        bullet_speed = 20
        bullet.x += bullet_speed * xv
        bullet.y += bullet_speed * yv
    bullet = [bullet for bullet in bullets if not is_offscreen(bullet.x, bullet.y)]


def draw_bullets():
    for bullet in bullets:
        ellipse((255,255,0), bullet.x, bullet.y, 20, 20)


def bullet_collisions(ghosts):
    bullet_radius = 10
    # for simplicitys sake we threat the ghosts as circles during intersections
    ghost_radius = 28.5 
    for bullet in bullets:
        for ghost in ghosts:
            d = distance(ghost.x, ghost.y, bullet.x, bullet.y)
            if d < bullet_radius + ghost_radius:
                ghosts.remove(ghost)
