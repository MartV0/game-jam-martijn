from jorcademy import *
import math
import random


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


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class Ghost:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed


w, h = 1500, 800
plane1 = Plane(100,700,0,True,'flight/plane_red_right.png')
plane2 = Plane(1400,700,0,False,'flight/plane_red_left.png')
maxplanespeed = 750
speedconstant = 1/100
lasers = []
laserdelay = 0
bullets = []
bulletdelay = 0
ghosts = []


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
    update_bullets()
    update_ghosts()
    bullet_collisions()


def update_ghosts():
    roll = random.randint(0,120)
    if roll == 20:
        x = random.randint(0, w)
        y = random.randint(0, h)
        d = random.randint(0, 359)
        ghosts.append(Ghost(x, y, d, 0))
    for ghost in ghosts:
        ghost.direction += random.randint(-10,10)
        vx, vy = get_direction_vector(ghost.direction, False)
        speed = 2
        ghost.x += speed * vx
        ghost.y += speed * vy
        ghost.x, ghost.y = teleport_if_offscreen((ghost.x, ghost.y), False)


def update_bullets():
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


def is_offscreen(x, y):
    return x < 0 or y < 0 or x > 1500 or y > 800



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


def update_laser(laser):
    laser.count -= 1
    if laser.count == 0:
        lasers.remove(laser)


def get_direction_vector(angle, right):
    radian = angle/360*2*math.pi
    if not right:
        radian += math.pi
    x = math.cos(radian)
    y = math.sin(radian)
    y *= -1
    return (x, y)


def teleport_if_offscreen(coordinates, teleport = True):
    x,y = coordinates
    if x>1500 and teleport:
        x=0
    elif x>1500:
        x=1500
    elif x<0 and teleport:
        x=1500
    elif x<0:
        x=0
    if y<0:
        y=0
    elif y>800:
        y=800
    return (x,y)


def laser_event(plane):
    global laserdelay
    if laserdelay <= 0:
        laser_length = 2000
        xv, yv = get_direction_vector(plane.angle, plane.right)
        x = plane.x + xv*(laser_length/2 + 30)
        y = plane.y + yv*(laser_length/2 + 30)
        lasers.append(Laser(x, y, plane.angle, 20))
        laserdelay = 30


def bullet_collisions():
    bullet_radius = 10
    # for simplicitys sake we threat the ghosts as cirkels during intersections
    ghost_radius = 28.5 
    for bullet in bullets:
        for ghost in ghosts:
            distance = ((bullet.x-ghost.x)**2 + (bullet.y-ghost.y)**2)**0.5
            if distance < bullet_radius + ghost_radius:
                ghosts.remove(ghost)



def draw() -> None:
    backdrop((50,150,255))
    draw_lasers(lasers)
    # draw_plane(plane1)
    draw_plane(plane2)
    draw_bullets(bullets)
    draw_ghosts(ghosts)


def draw_plane(plane: Plane) -> None:
    image(plane.sprite_url, plane.x, plane.y, 5, plane.angle)


def draw_lasers(lasers):
    for laser in lasers:
        rect((255,0,0), laser.x, laser.y, 2000, 10, laser.angle)


def draw_bullets(bullets):
    for bullet in bullets:
        ellipse((255,255,0), bullet.x, bullet.y, 20, 20)


def draw_ghosts(ghosts):
    for ghost in ghosts:
        # ellipse((0,255,0), ghost.x, ghost.y, 57, 57) 
        image("flight/ghost.png", ghost.x, ghost.y, 4, 0)
