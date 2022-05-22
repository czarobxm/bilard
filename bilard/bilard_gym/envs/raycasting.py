from .ball import *
import numpy as np
from pymunk import Vec2d

class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + " " + str(self.b) + "\n"

def cast(vec, wall):
    x1 = wall.a.x
    y1 = wall.a.y
    x2 = wall.b.x
    y2 = wall.b.y

    x4 = vec.a.x
    y4 = vec.a.y
    x3 = vec.b.x
    y3 = vec.b.y
    
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
    
    if t > 0 and t < 1 and u > 0:
        return Vec2d(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    else:
        return

def intersect(vec, table):
    for wall in table.positions():
        intersection = cast(vec, wall)
        if intersection is not None:
            return intersection
    
def raycast(table, n = 60):
    position = Vec2d(convert_coordinates(white_ball_full.body.position)[0], convert_coordinates(white_ball_full.body.position)[1])
    points_of_intersection = []

    for radius in range(0, 360, 360//n):

        r = Vec2d(5, 0)
        r = r.rotated_degrees(radius)
        r = r + position
        vec = Vector(position, r)
        
        intersection = intersect(vec, table)
        if intersection is not None:
            points_of_intersection.append(intersect(vec, table))

    return points_of_intersection


    