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


plane1 = Plane(100,700,0,True,'flight/plane_red_right.png')
plane2 = Plane(1400,700,0,False,'flight/plane_red_left.png')
maxplanespeed = 1000
speedconstant = 1/100

def setup() -> None:
    screen(1500,800)


def update() -> None:
    update_objects()
    draw()


def update_objects() -> None:
    update_plane(plane1)


def update_plane(plane):
    if is_key_down("space") and plane.speed < maxplanespeed:
        plane.speed+=1
    elif plane.speed>0:
        plane.speed-=1
    if is_key_down("d"):
        plane.angle-=3
    if is_key_down("f"):
        plane.angle+=3
    radian = plane.angle/360*2*math.pi
    if plane.right:
        radian*=-1
    x_speed = math.cos(radian) * speedconstant * plane.speed
    y_speed = math.sin(radian) * speedconstant * plane.speed
    plane.x += x_speed
    plane.y += y_speed




def draw() -> None:
    backdrop((50,150,255))
    draw_plane(plane1)
    draw_plane(plane2)


def draw_plane(plane: Plane) -> None:
    image(plane.sprite_url, plane.x, plane.y, 5, plane.angle)

