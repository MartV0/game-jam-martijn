from flight.coordinates import *
from jorcademy import *
import flight.bullet as bullet


shells = []
shelldelay = 0


def update_shells(plane):
    global shelldelay
    shelldelay -= 1
    if is_key_down('b') and shelldelay <= 0:
        shelldelay=20
        shells.append(bullet.create_bullet(plane))
    for shell in shells:
        bullet.move_bullet(shell)
    shell = [shell for shell in shells if not is_offscreen(shell.x, shell.y)]


def draw_shells():
    for shell in shells:
        ellipse((0,255,0), shell.x, shell.y, 20, 20)


def shell_collisions(ghosts):
    shell_radius = 10
    # for simplicitys sake we threat the ghosts as circles during intersections
    ghost_radius = 28.5 
    for shell in shells:
        for ghost in ghosts:
            d = distance(ghost.x, ghost.y, shell.x, shell.y)
            if d < shell_radius + ghost_radius:
                ghosts.remove(ghost)
                shell.direction = mirror_angle(shell.direction)


def mirror_angle(angle):
    angle += 90
    angle %= 360
    if (angle<0):
        angle += 360
    if (angle < 180):
        angle *= -1
    else: 
        angle -= 2*(angle-180)
    angle -= 90
    return angle
