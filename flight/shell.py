from flight.coordinates import *
from jorcademy import *
import flight.bullet as bullet


def update_shells(plane):
    plane.shelldelay -= 1
    if is_key_down('b') and plane.shelldelay <= 0:
        plane.shelldelay=20
        plane.shells.append(bullet.create_bullet(plane))
    for shell in plane.shells:
        bullet.move_bullet(shell)
        if is_offscreen(shell.x, shell.y):
            bounce_shell(shell, plane.shells)
    


def draw_shells(shells):
    for shell in shells:
        image("flight/koopa_shell.png", shell.x, shell.y, 2, 0)


def bounce_shell(shell, shells):
    shell.direction = bounce_angle(shell.direction)
    try:
        shell.bounce_count -= 1
        if shell.bounce_count < 0:
            shells.remove(shell)
    except AttributeError:
        shell.bounce_count = 4

def shell_collisions(plane, ghosts):
    shell_radius = 15
    # for simplicitys sake we threat the ghosts as circles during intersections
    ghost_radius = 28.5 
    for shell in plane.shells:
        for ghost in ghosts:
            d = distance(ghost.x, ghost.y, shell.x, shell.y)
            if d < shell_radius + ghost_radius:
                ghosts.remove(ghost)
                bounce_shell(shell, plane.shells)
