from jorcademy import *
import flight.laser as laser
import flight.plane as plane
import flight.bullet as bullet
import flight.shell as shell
import flight.ghost as ghost
import flight.fireball as fireball


def setup() -> None:
    screen(1500,800)
    add_key_down_event('g', lambda : laser.laser_event(plane.plane1))


def update() -> None:
    update_objects()
    draw()


def update_objects() -> None:
    plane.update_plane(plane.plane1)
    laser.update_lasers(plane.plane1)
    # bullet.update_bullets(plane.plane1)
    # shell.update_shells(plane.plane1)
    fireball.update_fireballs(plane.plane1)
    ghost.update_ghosts()
    # bullet.bullet_collisions(plane.plane1, ghost.ghosts)
    # shell.shell_collisions(plane.plane1, ghost.ghosts)
    fireball.fireball_collisions(plane.plane1, ghost.ghosts)
    laser.laser_collisions(plane.plane1, ghost.ghosts)


def draw() -> None:
    backdrop((50,150,255))
    laser.draw_lasers(plane.plane1.lasers)
    plane.draw_plane(plane.plane1)
    plane.draw_plane(plane.plane2)
    # shell.draw_shells(plane.plane1.shells)
    # bullet.draw_bullets(plane.plane1.bullets)
    fireball.draw_fireballs(plane.plane1.bullets)
    ghost.draw_ghosts()
