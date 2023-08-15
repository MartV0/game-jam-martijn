from jorcademy import *
from flight.coordinates import *


class Plane:
    def __init__(self, x, y, angle, right, sprite_url):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0
        self.right = right
        self.sprite_url = sprite_url


plane1 = Plane(100,700,0,True,'flight/plane_red_right.png')
plane2 = Plane(1400,700,0,False,'flight/plane_red_left.png')
maxplanespeed = 750
speedconstant = 1/100


def update_plane(plane):
    if is_key_down("space") and plane.speed < maxplanespeed:
        plane.speed+=10
    elif plane.speed>0:
        plane.speed-=4
    if is_key_down("d"):
        plane.angle-=3.5
    if is_key_down("f"):
        plane.angle+=3.5
    x_speed, y_speed = get_direction_vector(plane.angle, plane.right)
    x_speed *= speedconstant * plane.speed
    y_speed *= speedconstant * plane.speed
    plane.x += x_speed
    plane.y += y_speed
    plane.x, plane.y = teleport_if_offscreen((plane.x, plane.y))


def draw_plane(plane: Plane) -> None:
    image(plane.sprite_url, plane.x, plane.y, 5, plane.angle)
