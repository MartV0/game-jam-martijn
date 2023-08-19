from flight.coordinates import *
from jorcademy import *


laser_length = 880


class Laser:
    def __init__(self, x, y, angle, count):
        self.x = x
        self.y = y
        self.angle = angle
        self.count = count


def update_lasers(plane):
    if plane.laserdelay > 0:
        plane.laserdelay -= 1
    for laser in plane.lasers:
        update_laser(laser, plane)


def update_laser(laser, plane):
    laser.count -= 1
    if laser.count == 0:
        plane.lasers.remove(laser)


def laser_event(plane):
    if plane.laserdelay <= 0:
        xv, yv = get_direction_vector(plane.angle, plane.right)
        x = plane.x + xv*(laser_length/2 + 30)
        y = plane.y + yv*(laser_length/2 + 30)
        plane.lasers.append(Laser(x, y, plane.angle, 20))
        plane.laserdelay = 30


def draw_lasers(lasers):
    for laser in lasers:
        # rect((255,0,0), laser.x, laser.y, 2000, 10, laser.angle)
        image("flight/lightning_bolt.png", laser.x, laser.y, 4, laser.angle - 90)


def laser_collisions(plane, ghosts):
    laser_thickness = 5
    ghost_radius = 28.5
    for laser in plane.lasers:
        vx, vy = get_direction_vector(laser.angle)
        m = vy / vx
        b = laser.y - m*laser.x 
        for ghost in ghosts:
            m2 = -1 / m
            b2 = ghost.y - m2 * ghost.x
            x = (b - b2) / (m2 - m)
            y = m2 * x + b2
            d = distance(x, y, ghost.x, ghost.y)
            if d < 5 + 28.5 and distance(laser.x, laser.y, ghost.x, ghost.y) < laser_length/2:
                ghosts.remove(ghost)

