import math


w, h = 1500, 800


def is_offscreen(x, y):
    return x < 0 or y < 0 or x > w or y > h


def get_direction_vector(angle, right = False):
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
            

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def bounce_angle(angle):
    angle %= 360
    if (angle<0):
        angle += 360

    if angle > 45 and angle <= 135:
        angle *= -1
    elif angle > 135 and angle <= 225:
        angle = 2*90 - angle
    elif angle > 225 and angle <= 315:
        angle = 2*180 - angle
    else:
        angle = 2*270 - angle
    return angle
