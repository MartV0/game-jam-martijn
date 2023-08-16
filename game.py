from jorcademy import *
import flight.laser as laser
import flight.plane as plane
import flight.bullet as bullet
import flight.shell as shell
import flight.ghost as ghost


def setup() -> None:
    screen(1500,800)
    add_key_down_event('g', lambda : laser.laser_event(plane.plane1))


def update() -> None:
    update_objects()
    draw()


def update_objects() -> None:
    plane.update_plane(plane.plane1)
    laser.update_lasers()
    shell.update_shells(plane.plane1)
    ghost.update_ghosts()
    # bullet.bullet_collisions(ghost.ghosts)
    shell.shell_collisions(ghost.ghosts)
    laser.laser_collisions(ghost.ghosts)


def draw() -> None:
    backdrop((50,150,255))
    laser.draw_lasers()
    plane.draw_plane(plane.plane1)
    plane.draw_plane(plane.plane2)
    shell.draw_shells()
    ghost.draw_ghosts()
