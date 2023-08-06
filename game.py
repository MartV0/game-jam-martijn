from jorcademy import *
import math


class Plane:
    def __init__(self, x, y, angle, right, sprite_url):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0
        self.right = right
        self.sprite_url = sprite_url


class Laser:
    def __init__(self, x, y, angle, count):
        self.x = x
        self.y = y
        self.angle = angle
        self.count = count


plane1 = Plane(100,700,0,True,'flight/plane_red_right.png')
plane2 = Plane(1400,700,0,False,'flight/plane_red_left.png')
maxplanespeed = 1500
speedconstant = 1/100
lasers = []
laserdelay = 0

def setup() -> None:
    screen(1500,800)
    add_key_down_event('g', lambda : laser_event(plane2))



def update() -> None:
    update_objects()
    draw()


def update_objects() -> None:
    update_plane(plane2)
    for laser in lasers:
        update_laser(laser)
    global laserdelay
    if laserdelay > 0:
        laserdelay -= 1


def update_plane(plane):
    if is_key_down("space") and plane.speed < maxplanespeed:
        plane.speed+=10
    elif plane.speed>0:
        plane.speed-=4
    if is_key_down("d"):
        plane.angle-=5
    if is_key_down("f"):
        plane.angle+=5
    x_speed, y_speed = get_plane_direction_vector(plane)
    x_speed *= speedconstant * plane.speed
    y_speed *= speedconstant * plane.speed
    plane.x += x_speed
    plane.y += y_speed
    plane.x, plane.y = teleport_if_offscreen((plane.x, plane.y))


def update_laser(laser):
    laser.count -= 1
    if laser.count == 0:
        lasers.remove(laser)


def get_plane_direction_vector(plane):
    radian = plane.angle/360*2*math.pi
    if not plane.right:
        radian += math.pi
    x = math.cos(radian)
    y = math.sin(radian)
    y *= -1
    return (x, y)


def teleport_if_offscreen(coordinates):
    x,y = coordinates
    if x>1500:
        x=0
    elif x<0:
        x=1500
    if y<0:
        y=0
    elif y>800:
        y=800
    return (x,y)


def laser_event(plane):
    global laserdelay
    if laserdelay <= 0:
        laser_length = 2000
        xv, yv = get_plane_direction_vector(plane)
        x = plane.x + xv*(laser_length/2 + 30)
        y = plane.y + yv*(laser_length/2 + 30)
        lasers.append(Laser(x, y, plane.angle, 20))
        laserdelay = 30


def draw() -> None:
    backdrop((50,150,255))
    draw_lasers(lasers)
    draw_plane(plane1)
    draw_plane(plane2)


def draw_plane(plane: Plane) -> None:
    image(plane.sprite_url, plane.x, plane.y, 5, plane.angle)


def draw_lasers(lasers):
    for laser in lasers:
        rect((255,0,0), laser.x, laser.y, 2000, 10, laser.angle)


